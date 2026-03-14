drop database if exists graph;
create database graph;
use graph;

create table node (
 node_id int primary key,
 type varchar(20)
 );
 
 create table edge (
 edge_id int primary key,
  in_node int,
  out_node int,
  type varchar(20)
  );
  
create table node_props (
  node_id int,
  propkey varchar(20),
  string_value varchar(100),
  num_value double
  );
  
 
 insert into node values 
 (1,'Person'),
 (2,'Person'),
 (3,'Person'),
 (4,'Person'),
 (5,'Person'),
 (6,'Book'),
 (7,'Book'),
 (8,'Book'),
 (9,'Book');
 
 insert into node_props values
 (1, 'name', 'Emily', null),
 (2, 'name', 'Spencer', null),
 (3, 'name', 'Brendan', null),
 (4, 'name', 'Trevor', null),
 (5, 'name', 'Paxton', null),
 (6, 'title', 'Cosmos', null),
 (6, 'price', null, 17.00),
 (7, 'title', 'Database Design', null),
 (7, 'price', null, 195.00),
 (8, 'title', 'The Life of Cronkite', null),
 (8, 'price', null, 29.95),
 (9, 'title', 'DNA and you', null),
 (9, 'price', null, 11.50);
 
 insert into edge values
 (1, 1, 7, 'bought'),
 (2, 2, 6, 'bought'),
 (3, 2, 7, 'bought'),
 (4, 3, 7, 'bought'),
 (5, 3, 9, 'bought'),
 (6, 4, 6, 'bought'),
 (7, 4, 7, 'bought'), 
 (8, 5, 7, 'bought'),
 (9, 5, 8, 'bought'),
 (10, 1,2,'knows'),
 (11, 2, 1, 'knows'),
 (12, 2, 3, 'knows');
 
 
-- a. what is the sum of all book prices?
    SELECT SUM(num_value) AS total_price
    FROM node_props
    WHERE propkey = 'price';

-- b. how many people bought each book?
-- Give title and number of times purchased
    SELECT np.string_value AS title, COUNT(*) AS times_purchased
    FROM edge e
    JOIN node_props np ON e.out_node = np.node_id AND np.propkey = 'title'
    WHERE e.type = 'bought'
    GROUP BY np.string_value;


-- c. What is the most expensive book?
-- Give title and price
    SELECT np_title.string_value AS title, np_price.num_value AS price
    FROM node_props np_title
    JOIN node_props np_price ON np_title.node_id = np_price.node_id
    WHERE np_title.propkey = 'title'
      AND np_price.propkey = 'price'
      AND np_price.num_value = (
          SELECT MAX(num_value) FROM node_props WHERE propkey = 'price'
      );


-- d. Who does spencer know?
    SELECT np_known.string_value AS name
    FROM node_props np_spencer
    JOIN node n_spencer ON np_spencer.node_id = n_spencer.node_id
    JOIN edge e ON e.in_node = n_spencer.node_id AND e.type = 'knows'
    JOIN node_props np_known ON e.out_node = np_known.node_id AND np_known.propkey = 'name'
    WHERE np_spencer.propkey = 'name'
      AND np_spencer.string_value = 'Spencer';


-- e. What books did spencer buy?  Give title and price.
    SELECT np_title.string_value AS title, np_price.num_value AS price
    FROM node_props np_spencer
    JOIN edge e ON e.in_node = np_spencer.node_id AND e.type = 'bought'
    JOIN node_props np_title ON e.out_node = np_title.node_id AND np_title.propkey = 'title'
    JOIN node_props np_price ON e.out_node = np_price.node_id AND np_price.propkey = 'price'
    WHERE np_spencer.propkey = 'name'
      AND np_spencer.string_value = 'Spencer';



-- f. Who knows each other?
    SELECT np1.string_value AS person1, np2.string_value AS person2
    FROM edge e1
    JOIN edge e2 ON e1.in_node = e2.out_node AND e1.out_node = e2.in_node
    JOIN node_props np1 ON e1.in_node = np1.node_id AND np1.propkey = 'name'
    JOIN node_props np2 ON e1.out_node = np2.node_id AND np2.propkey = 'name'
    WHERE e1.type = 'knows'
      AND e2.type = 'knows'
      AND e1.in_node < e1.out_node;


-- g. What books were purchased by people who spencer knows?
-- You just have to combine two previous queries
-- Dropping price attribute in the process
    SELECT np_title.string_value AS title
    FROM node_props np_spencer
    JOIN node n_spencer ON np_spencer.node_id = n_spencer.node_id
    JOIN edge e_knows ON e_knows.in_node = n_spencer.node_id AND e_knows.type = 'knows'
    JOIN edge e_bought ON e_bought.in_node = e_knows.out_node AND e_bought.type = 'bought'
    JOIN node_props np_title ON e_bought.out_node = np_title.node_id AND np_title.propkey = 'title'
    WHERE np_spencer.propkey = 'name'
      AND np_spencer.string_value = 'Spencer';




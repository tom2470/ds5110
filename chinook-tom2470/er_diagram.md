
# Entity-Relationship Diagrams

* An E-R model is usually the result of systematic analysis to define and organize data needed in an area of a business.
* Typically, it represents records of entities and events monitored and directed by business processes, 
  rather than the processes themselves.
* It is usually drawn in a graphical form as boxes (entities) that are connected by lines (relationships) 
  that encode the associations and dependencies.
* Ref: [ER diagram](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) -- wikipedia
  * Each row of a table represents on instance of an entity type
  * Each field in a table represents an attribute type
  * Entity relationships are implemented with primary key and foreign keys.
  * The primary key of one entity is a pointer or foreign key to the table of another entity
* Toy example: [students ERD](https://observablehq.com/d/2edf02959e5d03fe) -- my notebook

## Some examples

* [students ER diagram](https://observablehq.com/d/2edf02959e5d03fe)
* [chinook ER diagram](https://observablehq.com/@pbogden/chinook-er-diagram)
* [SQL.js](https://sql.js.org/) -- a JavaScript implementation of SQLite -- sql.js.org 
* [Chinook ER diagram](https://observablehq.com/d/64c467df985eb151) -- my notebook
  * This indicates the primary keys
* [SQLite ER diagram](https://observablehq.com/@randomfractals/sqlite-er-diagram) for chinook.db -- observable notebook
  * This shows explicit PK and FK relationships
* [Dataset foreign key diagram](https://observablehq.com/d/a654b8756ea5061b) by Thomas Ballinger -- observable notebook
  * Earlier version

## PRAGMA statements

These are used to get the entity relationships and table info for the diagrams

* [PRAGMA statements](https://www.sqlite.org/pragma.html) extend SQL (e.g., to query non-table data) -- sqlite.org
* [Primary key](https://en.wikipedia.org/wiki/Primary_key) -- wikipedia
  * A primary key (PK) is a set of attributes (columns) that uniquely specify a tuple (row) in a relation
  * List primary keys in SQLite with a PRAGMA statement: `PRAGMA schema.index_list(table-name);`
* [Foreign key](https://en.wikipedia.org/wiki/Foreign_key) -- wikipedia
  * A foreign key (FK) is a set of attributes in one table that refers to the primary key of another table
  * The foreign key links the two tables
  * List foreign keys in SQLite with a PRAGMA statement: `PRAGMA [database.]foreign_key_list( table_name );`
  * Ref: [foreign_key_list](https://www.sqlite.org/pragma.html#pragma_foreign_key_list) -- sqlite.org
* [Database index](https://en.wikipedia.org/wiki/Database_index) -- wikipedia
  * a data structure that improves the speed of data retrieval operations at the cost of additional writes and storage

## Count open connections

List open database connections

```
lsof chinook.db
```

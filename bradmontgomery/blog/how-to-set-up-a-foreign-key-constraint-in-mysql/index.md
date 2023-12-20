---
date: '2009-04-01T14:49:00+00:00'
title: How to Set up a Foreign Key Constraint in MySQL
draft: false
tags:
- Programming
- mysql
- web
slug: how-to-set-up-a-foreign-key-constraint-in-mysql
description: ''
markup: md
url: /blog/how-to-set-up-a-foreign-key-constraint-in-mysql/
aliases:
- /blog/2009/04/01/how-to-set-up-a-foreign-key-constraint-in-mysql/

---

The default [storage engine](http://dev.mysql.com/doc/refman/5.0/en/storage-engines.html) in MySQL ([MyISAM](http://dev.mysql.com/doc/refman/5.0/en/myisam-storage-engine.html)) does not support Foreign Key constraints. If you want to use Foreign Keys in Mysql, you need to use [InnoDB](http://dev.mysql.com/doc/refman/5.0/en/using-innodb-tables.html).

  
The following is a simple example that illustrates Foreign Key constraints, we'll create tables to store information about Authors and their Books. The Foreign key will link a book to an Author. Note, that in MySQL we need to use the [InnoDB](http://dev.mysql.com/doc/refman/5.0/en/using-innodb-tables.html) storage engine to support [Foreign Key Constraints](http://dev.mysql.com/doc/refman/5.0/en/innodb-foreign-key-constraints.html).

  
First, we need to create a simple table for Authors. There are only two columns: a primary key and the author's name


```
CREATE TABLE author (id integer primary key auto_increment, name text) ENGINE=InnoDB;
```
  
Next, we create a simple table for Books. Again, we need a primary key (id), the title of the book, and the column that will be used as the Foreign Kye (author\_id). The author\_id column will be a Foreign Key that references the author table's id column (i.e. it's primary key).

  

```
CREATE TABLE books (id integer primary key auto_increment, title text, author_id integer NOT NULL) ENGINE=InnoDB;
```
  
Finally, we alter the books table to add the Foreign Key constraint. Below, the *author\_id\_refs* is just a name for the constraint, and this could be anything that we want (as long as it's sensible!)

  

```
ALTER TABLE `books` ADD CONSTRAINT author_id_refs FOREIGN KEY (`author_id`) REFERENCES `author` (`id`);
```
  
Another example is available in the MySQL documentation that covers [Foreign Key Constraints](http://dev.mysql.com/doc/refman/5.0/en/innodb-foreign-key-constraints.html).

  
An Example
----------

  
Insert a couple of Authors:

  

```
insert into author (name) values ('Brad Montgomery');  
insert into author (name) values ('John Doe');
```
  
Let's see what's in the author table:

  

```
  
mysql> select * from author;  
+----+-----------------+  
| id | name            |  
+----+-----------------+  
|  1 | Brad Montgomery |   
|  2 | John Doe        |   
+----+-----------------+  
2 rows in set (0.00 sec)  

```
  
Lets put some stuff in the Books table. Note that author\_id column corresponds to the id column in the author table above.

  

```
insert into books (title, author_id) values ('Brads book', 1);  
insert into books (title, author_id) values ('John Does book', 2);
```
  
  
Lets see what the books table looks like and what's in it:

  

```
  
mysql> describe books;  
+-----------+---------+------+-----+---------+----------------+  
| Field     | Type    | Null | Key | Default | Extra          |  
+-----------+---------+------+-----+---------+----------------+  
| id        | int(11) | NO   | PRI | NULL    | auto_increment |   
| title     | text    | YES  |     | NULL    |                |   
| author_id | int(11) | NO   | MUL | NULL    |                |   
+-----------+---------+------+-----+---------+----------------+  
3 rows in set (0.00 sec)  
  
mysql> select * from books;  
+----+----------------+-----------+  
| id | title          | author_id |  
+----+----------------+-----------+  
|  1 | Brads book     |         1 |   
|  2 | John Does book |         2 |   
+----+----------------+-----------+  
2 rows in set (0.00 sec)  

```
  
  
Try to Delete Something
-----------------------

  
When you try to delete an author, an Error will occur

  

```
delete from author where id=2;  
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails   
(`brad/books`, CONSTRAINT `author_id_refs` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`))  

```
  
This happens because the data in the books table depends on the data in the author table. The Default constraint prevents you from deleting these books, without first deleting the author

  

```
  
mysql> delete from books where author_id=2;  
Query OK, 1 row affected (0.00 sec)  
  
mysql> delete from author where id=2;  
Query OK, 1 row affected (0.01 sec)
```
  
When you delete the author's books first, the author no longer has any dependencies. You can therefore delete the author.

![](https://blogger.googleusercontent.com/tracker/4123748873183487963-4345063366065028230?l=bradmontgomery.blogspot.com)
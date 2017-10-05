dbx=# table empsalary 
dbx-# ;
  depname  | empno | salary | enroll_date 
-----------+-------+--------+-------------
 develop   |    10 |   5200 | 2007-08-01
 sales     |     1 |   5000 | 2006-10-01
 personnel |     5 |   3500 | 2007-12-10
 sales     |     4 |   4800 | 2007-08-08
 personnel |     2 |   3900 | 2006-12-23
 develop   |     7 |   4200 | 2008-01-01
 develop   |     9 |   4500 | 2008-01-01
 sales     |     3 |   4800 | 2007-08-01
 develop   |     8 |   6000 | 2006-10-01
 develop   |    11 |   5200 | 2007-08-15
(10 rows)


dbx=# SELECT depname, empno, salary, sum(salary) OVER (PARTITION BY depname) FROM empsalary ORDER BY depname, salary;
  depname  | empno | salary |  sum  
-----------+-------+--------+-------
 develop   |     7 |   4200 | 25100
 develop   |     9 |   4500 | 25100
 develop   |    11 |   5200 | 25100
 develop   |    10 |   5200 | 25100
 develop   |     8 |   6000 | 25100
 personnel |     5 |   3500 |  7400
 personnel |     2 |   3900 |  7400
 sales     |     3 |   4800 | 14600
 sales     |     4 |   4800 | 14600
 sales     |     1 |   5000 | 14600
(10 rows)


dbx=# explain analyze verbose SELECT depname, empno, salary, sum(salary) OVER (PARTITION BY depname) FROM empsalary ORDER BY depname, salary;
                                                             QUERY PLAN                                                              
-------------------------------------------------------------------------------------------------------------------------------------
 Sort  (cost=147.10..149.78 rows=1070 width=52) (actual time=0.363..0.393 rows=10 loops=1)
   Output: depname, empno, salary, (sum(salary) OVER (?))
   Sort Key: empsalary.depname, empsalary.salary
   Sort Method: quicksort  Memory: 25kB
   ->  WindowAgg  (cost=74.54..93.26 rows=1070 width=52) (actual time=0.163..0.299 rows=10 loops=1)
         Output: depname, empno, salary, sum(salary) OVER (?)
         ->  Sort  (cost=74.54..77.21 rows=1070 width=44) (actual time=0.108..0.140 rows=10 loops=1)
               Output: depname, empno, salary
               Sort Key: empsalary.depname
               Sort Method: quicksort  Memory: 25kB
               ->  Seq Scan on pg_temp_2.empsalary  (cost=0.00..20.70 rows=1070 width=44) (actual time=0.015..0.049 rows=10 loops=1)
                     Output: depname, empno, salary
 Planning time: 0.168 ms
 Execution time: 0.534 ms
(14 rows)


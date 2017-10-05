dbx=# explain analyze verbose SELECT '' AS "xxx", *
FROM J1_TBL t1 (a, b, c) cross JOIN J2_TBL t2 (a, d);
                                                         QUERY PLAN                                                         
----------------------------------------------------------------------------------------------------------------------------
 Nested Loop  (cost=0.00..33957.60 rows=2712000 width=80) (actual time=0.085..2.520 rows=99 loops=1)
   Output: '', t1.a, t1.b, t1.c, t2.a, t2.d
   ->  Seq Scan on public.j2_tbl t2  (cost=0.00..32.60 rows=2260 width=8) (actual time=0.030..0.089 rows=9 loops=1)
         Output: t2.a, t2.d
   ->  Materialize  (cost=0.00..28.00 rows=1200 width=40) (actual time=0.009..0.092 rows=11 loops=9)
         Output: t1.a, t1.b, t1.c
         ->  Seq Scan on public.j1_tbl t1  (cost=0.00..22.00 rows=1200 width=40) (actual time=0.012..0.081 rows=11 loops=1)
               Output: t1.a, t1.b, t1.c
 Planning time: 0.230 ms
 Execution time: 3.307 ms
(10 rows)



dbx=# explain analyze verbose SELECT '' AS "xxx", *
FROM J1_TBL t1 (a, b, c) cross JOIN J2_TBL t2 (a, d) ORDER BY t1.a;
                                                            QUERY PLAN                                                            
----------------------------------------------------------------------------------------------------------------------------------
 Sort  (cost=583300.35..590080.35 rows=2712000 width=84) (actual time=3.110..3.662 rows=99 loops=1)
   Output: '', t1.a, t1.b, t1.c, t2.a, t2.d, t1.a
   Sort Key: t1.a
   Sort Method: quicksort  Memory: 32kB
   ->  Nested Loop  (cost=0.00..33957.60 rows=2712000 width=84) (actual time=0.085..2.296 rows=99 loops=1)
         Output: '', t1.a, t1.b, t1.c, t2.a, t2.d, t1.a
         ->  Seq Scan on public.j2_tbl t2  (cost=0.00..32.60 rows=2260 width=8) (actual time=0.030..0.084 rows=9 loops=1)
               Output: t2.a, t2.d
         ->  Materialize  (cost=0.00..28.00 rows=1200 width=40) (actual time=0.008..0.091 rows=11 loops=9)
               Output: t1.a, t1.b, t1.c
               ->  Seq Scan on public.j1_tbl t1  (cost=0.00..22.00 rows=1200 width=40) (actual time=0.012..0.120 rows=11 loops=1)
                     Output: t1.a, t1.b, t1.c
 Planning time: 0.524 ms
 Execution time: 4.498 ms
(14 rows)




dbx-#   FROM J1_TBL JOIN J2_TBL ON (J1_TBL.i <= J2_TBL.k);
 xxx | i | j |   t   | i | k 
-----+---+---+-------+---+---
     | 1 | 4 | one   | 2 | 2
     | 2 | 3 | two   | 2 | 2
     | 0 |   | zero  | 2 | 2
     | 1 | 4 | one   | 2 | 4
     | 2 | 3 | two   | 2 | 4
     | 3 | 2 | three | 2 | 4
     | 4 | 1 | four  | 2 | 4
     | 0 |   | zero  | 2 | 4
     | 0 |   | zero  |   | 0
(9 rows)

dbx=# explain analyze verbose SELECT '' AS "xxx", *
FROM J1_TBL JOIN J2_TBL ON (J1_TBL.i <= J2_TBL.k);

                                                       QUERY PLAN                                                        
-------------------------------------------------------------------------------------------------------------------------
 Nested Loop  (cost=0.00..40737.60 rows=904000 width=80) (actual time=0.433..1.901 rows=9 loops=1)
   Output: '', j1_tbl.i, j1_tbl.j, j1_tbl.t, j2_tbl.i, j2_tbl.k
   Join Filter: (j1_tbl.i <= j2_tbl.k)
   Rows Removed by Join Filter: 90
   ->  Seq Scan on public.j2_tbl  (cost=0.00..32.60 rows=2260 width=8) (actual time=0.031..0.088 rows=9 loops=1)
         Output: j2_tbl.i, j2_tbl.k
   ->  Materialize  (cost=0.00..28.00 rows=1200 width=40) (actual time=0.008..0.102 rows=11 loops=9)
         Output: j1_tbl.i, j1_tbl.j, j1_tbl.t
         ->  Seq Scan on public.j1_tbl  (cost=0.00..22.00 rows=1200 width=40) (actual time=0.013..0.123 rows=11 loops=1)
               Output: j1_tbl.i, j1_tbl.j, j1_tbl.t
 Planning time: 0.195 ms
 Execution time: 2.206 ms
(12 rows)


dbx=# explain analyze verbose SELECT '' AS "xxx", *
FROM J1_TBL JOIN J2_TBL ON (J1_TBL.i <> J2_TBL.i);
                                                       QUERY PLAN                                                        
-------------------------------------------------------------------------------------------------------------------------
 Nested Loop  (cost=0.00..40737.60 rows=2698440 width=80) (actual time=0.117..2.171 rows=56 loops=1)
   Output: '', j1_tbl.i, j1_tbl.j, j1_tbl.t, j2_tbl.i, j2_tbl.k
   Join Filter: (j1_tbl.i <> j2_tbl.i)
   Rows Removed by Join Filter: 43
   ->  Seq Scan on public.j2_tbl  (cost=0.00..32.60 rows=2260 width=8) (actual time=0.028..0.084 rows=9 loops=1)
         Output: j2_tbl.i, j2_tbl.k
   ->  Materialize  (cost=0.00..28.00 rows=1200 width=40) (actual time=0.008..0.102 rows=11 loops=9)
         Output: j1_tbl.i, j1_tbl.j, j1_tbl.t
         ->  Seq Scan on public.j1_tbl  (cost=0.00..22.00 rows=1200 width=40) (actual time=0.013..0.084 rows=11 loops=1)
               Output: j1_tbl.i, j1_tbl.j, j1_tbl.t
 Planning time: 0.257 ms
 Execution time: 2.735 ms
(12 rows)


dbx=# explain analyze verbose SELECT '' AS "xxx", *
FROM J1_TBL LEFT JOIN J2_TBL USING (i)
ORDER BY i, k, t;

                                                          QUERY PLAN                                                           
-------------------------------------------------------------------------------------------------------------------------------
 Sort  (cost=1381.97..1415.87 rows=13560 width=76) (actual time=0.537..0.582 rows=13 loops=1)
   Output: '', j1_tbl.i, j1_tbl.j, j1_tbl.t, j2_tbl.k
   Sort Key: j1_tbl.i, j2_tbl.k, j1_tbl.t
   Sort Method: quicksort  Memory: 25kB
   ->  Merge Left Join  (cost=241.88..451.28 rows=13560 width=76) (actual time=0.218..0.453 rows=13 loops=1)
         Output: '', j1_tbl.i, j1_tbl.j, j1_tbl.t, j2_tbl.k
         Merge Cond: (j1_tbl.i = j2_tbl.i)
         ->  Sort  (cost=83.37..86.37 rows=1200 width=40) (actual time=0.115..0.155 rows=11 loops=1)
               Output: j1_tbl.i, j1_tbl.j, j1_tbl.t
               Sort Key: j1_tbl.i
               Sort Method: quicksort  Memory: 25kB
               ->  Seq Scan on public.j1_tbl  (cost=0.00..22.00 rows=1200 width=40) (actual time=0.019..0.059 rows=11 loops=1)
                     Output: j1_tbl.i, j1_tbl.j, j1_tbl.t
         ->  Sort  (cost=158.51..164.16 rows=2260 width=8) (actual time=0.087..0.111 rows=8 loops=1)
               Output: j2_tbl.k, j2_tbl.i
               Sort Key: j2_tbl.i
               Sort Method: quicksort  Memory: 25kB
               ->  Seq Scan on public.j2_tbl  (cost=0.00..32.60 rows=2260 width=8) (actual time=0.008..0.041 rows=9 loops=1)
                     Output: j2_tbl.k, j2_tbl.i
 Planning time: 0.198 ms
 Execution time: 0.773 ms
(21 rows)



dbx=# SELECT '' AS "xxx", *
dbx-#   FROM J1_TBL RIGHT OUTER JOIN J2_TBL USING (i);
 xxx | i | j |   t   | k  
-----+---+---+-------+----
     | 0 |   | zero  |   
     | 1 | 4 | one   | -1
     | 2 | 3 | two   |  2
     | 2 | 3 | two   |  4
     | 3 | 2 | three | -3
     | 5 | 0 | five  | -5
     | 5 | 0 | five  | -5
     |   |   |       |   
     |   |   |       |  0
(9 rows)
                                                       QUERY PLAN                                                        
-------------------------------------------------------------------------------------------------------------------------
 Merge Right Join  (cost=241.88..451.28 rows=13560 width=76) (actual time=0.513..0.802 rows=9 loops=1)
   Output: '', j2_tbl.i, j1_tbl.j, j1_tbl.t, j2_tbl.k
   Merge Cond: (j1_tbl.i = j2_tbl.i)
   ->  Sort  (cost=83.37..86.37 rows=1200 width=40) (actual time=0.325..0.362 rows=7 loops=1)
         Output: j1_tbl.j, j1_tbl.t, j1_tbl.i
         Sort Key: j1_tbl.i
         Sort Method: quicksort  Memory: 25kB
         ->  Seq Scan on public.j1_tbl  (cost=0.00..22.00 rows=1200 width=40) (actual time=0.033..0.107 rows=11 loops=1)
               Output: j1_tbl.j, j1_tbl.t, j1_tbl.i
   ->  Sort  (cost=158.51..164.16 rows=2260 width=8) (actual time=0.157..0.211 rows=9 loops=1)
         Output: j2_tbl.i, j2_tbl.k
         Sort Key: j2_tbl.i
         Sort Method: quicksort  Memory: 25kB
         ->  Seq Scan on public.j2_tbl  (cost=0.00..32.60 rows=2260 width=8) (actual time=0.019..0.072 rows=9 loops=1)
               Output: j2_tbl.i, j2_tbl.k
 Planning time: 0.391 ms
 Execution time: 1.028 ms
(17 rows)

dbx=# SELECT '' AS "xxx", *
dbx-#   FROM J1_TBL FULL OUTER JOIN J2_TBL USING (i)
dbx-#   ORDER BY i, k, t;
 xxx | i | j |   t   | k  
-----+---+---+-------+----
     | 0 |   | zero  |   
     | 1 | 4 | one   | -1
     | 2 | 3 | two   |  2
     | 2 | 3 | two   |  4
     | 3 | 2 | three | -3
     | 4 | 1 | four  |   
     | 5 | 0 | five  | -5
     | 5 | 0 | five  | -5
     | 6 | 6 | six   |   
     | 7 | 7 | seven |   
     | 8 | 8 | eight |   
     |   |   |       |  0
     |   |   | null  |   
     |   | 0 | zero  |   
     |   |   |       |   
(15 rows)

                                                          QUERY PLAN                                                           
-------------------------------------------------------------------------------------------------------------------------------
 Sort  (cost=1381.97..1415.87 rows=13560 width=76) (actual time=1.145..1.236 rows=15 loops=1)
   Output: '', (COALESCE(j1_tbl.i, j2_tbl.i)), j1_tbl.j, j1_tbl.t, j2_tbl.k
   Sort Key: (COALESCE(j1_tbl.i, j2_tbl.i)), j2_tbl.k, j1_tbl.t
   Sort Method: quicksort  Memory: 25kB
   ->  Merge Full Join  (cost=241.88..451.28 rows=13560 width=76) (actual time=0.425..0.913 rows=15 loops=1)
         Output: '', COALESCE(j1_tbl.i, j2_tbl.i), j1_tbl.j, j1_tbl.t, j2_tbl.k
         Merge Cond: (j1_tbl.i = j2_tbl.i)
         ->  Sort  (cost=83.37..86.37 rows=1200 width=40) (actual time=0.247..0.313 rows=11 loops=1)
               Output: j1_tbl.i, j1_tbl.j, j1_tbl.t
               Sort Key: j1_tbl.i
               Sort Method: quicksort  Memory: 25kB
               ->  Seq Scan on public.j1_tbl  (cost=0.00..22.00 rows=1200 width=40) (actual time=0.077..0.144 rows=11 loops=1)
                     Output: j1_tbl.i, j1_tbl.j, j1_tbl.t
         ->  Sort  (cost=158.51..164.16 rows=2260 width=8) (actual time=0.148..0.333 rows=9 loops=1)
               Output: j2_tbl.i, j2_tbl.k
               Sort Key: j2_tbl.i
               Sort Method: quicksort  Memory: 25kB
               ->  Seq Scan on public.j2_tbl  (cost=0.00..32.60 rows=2260 width=8) (actual time=0.013..0.065 rows=9 loops=1)
                     Output: j2_tbl.i, j2_tbl.k
 Planning time: 0.438 ms
 Execution time: 1.522 ms
(21 rows)



dbx=# SELECT * FROM t1 FULL JOIN t2 USING (name) FULL JOIN t3 USING (name);
 name | n  | n  | n  
------+----+----+----
 bb   | 11 | 12 | 13
 cc   |    | 22 | 23
 dd   |    |    | 33
 ee   |    | 42 |   
(4 rows)

dbx=# explain analyze verbose SELECT * FROM t1 FULL JOIN t2 USING (name) FULL JOIN t3 USING (name);
                                                           QUERY PLAN                                                           
--------------------------------------------------------------------------------------------------------------------------------
 Merge Full Join  (cost=915.09..1689.53 rows=51206 width=44) (actual time=0.629..0.736 rows=4 loops=1)
   Output: COALESCE(COALESCE(t1.name, t2.name), t3.name), t1.n, t2.n, t3.n
   Merge Cond: (t3.name = (COALESCE(t1.name, t2.name)))
   ->  Sort  (cost=88.17..91.35 rows=1270 width=36) (actual time=0.123..0.140 rows=3 loops=1)
         Output: t3.name, t3.n
         Sort Key: t3.name
         Sort Method: quicksort  Memory: 25kB
         ->  Seq Scan on public.t3  (cost=0.00..22.70 rows=1270 width=36) (actual time=0.029..0.048 rows=3 loops=1)
               Output: t3.name, t3.n
   ->  Sort  (cost=826.91..847.07 rows=8064 width=72) (actual time=0.480..0.498 rows=3 loops=1)
         Output: t1.name, t1.n, t2.name, t2.n, (COALESCE(t1.name, t2.name))
         Sort Key: (COALESCE(t1.name, t2.name))
         Sort Method: quicksort  Memory: 25kB
         ->  Merge Full Join  (cost=176.34..303.67 rows=8064 width=72) (actual time=0.336..0.410 rows=3 loops=1)
               Output: t1.name, t1.n, t2.name, t2.n, COALESCE(t1.name, t2.name)
               Merge Cond: (t1.name = t2.name)
               ->  Sort  (cost=88.17..91.35 rows=1270 width=36) (actual time=0.069..0.075 rows=1 loops=1)
                     Output: t1.name, t1.n
                     Sort Key: t1.name
                     Sort Method: quicksort  Memory: 25kB
                     ->  Seq Scan on public.t1  (cost=0.00..22.70 rows=1270 width=36) (actual time=0.016..0.023 rows=1 loops=1)
                           Output: t1.name, t1.n
               ->  Sort  (cost=88.17..91.35 rows=1270 width=36) (actual time=0.090..0.109 rows=3 loops=1)
                     Output: t2.name, t2.n
                     Sort Key: t2.name
                     Sort Method: quicksort  Memory: 25kB
                     ->  Seq Scan on public.t2  (cost=0.00..22.70 rows=1270 width=36) (actual time=0.012..0.029 rows=3 loops=1)
                           Output: t2.name, t2.n
 Planning time: 0.552 ms
 Execution time: 1.166 ms
(30 rows)


dbx=# SELECT * FROM t1 FULL JOIN t2 USING (name);
 name | n  | n  
------+----+----
 bb   | 11 | 12
 cc   |    | 22
 ee   |    | 42
(3 rows)

dbx=# explain analyze verbose SELECT * FROM t1 FULL JOIN t2 USING (name);
                                                     QUERY PLAN                                                     
--------------------------------------------------------------------------------------------------------------------
 Merge Full Join  (cost=176.34..303.67 rows=8064 width=40) (actual time=0.068..0.087 rows=3 loops=1)
   Output: COALESCE(t1.name, t2.name), t1.n, t2.n
   Merge Cond: (t1.name = t2.name)
   ->  Sort  (cost=88.17..91.35 rows=1270 width=36) (actual time=0.025..0.027 rows=1 loops=1)
         Output: t1.name, t1.n
         Sort Key: t1.name
         Sort Method: quicksort  Memory: 25kB
         ->  Seq Scan on public.t1  (cost=0.00..22.70 rows=1270 width=36) (actual time=0.010..0.012 rows=1 loops=1)
               Output: t1.name, t1.n
   ->  Sort  (cost=88.17..91.35 rows=1270 width=36) (actual time=0.033..0.038 rows=3 loops=1)
         Output: t2.name, t2.n
         Sort Key: t2.name
         Sort Method: quicksort  Memory: 25kB
         ->  Seq Scan on public.t2  (cost=0.00..22.70 rows=1270 width=36) (actual time=0.004..0.009 rows=3 loops=1)
               Output: t2.name, t2.n
 Planning time: 0.112 ms
 Execution time: 0.237 ms
(17 rows)




dbx=# SELECT * FROM
dbx-# (SELECT name, n as s1_n, 1 as s1_1 FROM t1) as s1
dbx-# NATURAL FULL JOIN
dbx-# (SELECT name, n as s2_n, 2 as s2_2 FROM t2) as s2
dbx-# NATURAL FULL JOIN
dbx-# (SELECT name, n as s3_n, 3 as s3_2 FROM t3) s3;
 name | s1_n | s1_1 | s2_n | s2_2 | s3_n | s3_2 
------+------+------+------+------+------+------
 bb   |   11 |    1 |   12 |    2 |   13 |    3
 cc   |      |      |   22 |    2 |   23 |    3
 dd   |      |      |      |      |   33 |    3
 ee   |      |      |   42 |    2 |      |     
(4 rows)


                                                           QUERY PLAN                                                           
--------------------------------------------------------------------------------------------------------------------------------
 Merge Full Join  (cost=915.09..1689.53 rows=51206 width=56) (actual time=0.566..0.675 rows=4 loops=1)
   Output: COALESCE(COALESCE(t1.name, t2.name), t3.name), t1.n, (1), t2.n, (2), t3.n, (3)
   Merge Cond: (t3.name = (COALESCE(t1.name, t2.name)))
   ->  Sort  (cost=88.17..91.35 rows=1270 width=40) (actual time=0.129..0.148 rows=3 loops=1)
         Output: t3.name, t3.n, (3)
         Sort Key: t3.name
         Sort Method: quicksort  Memory: 25kB
         ->  Seq Scan on public.t3  (cost=0.00..22.70 rows=1270 width=40) (actual time=0.033..0.053 rows=3 loops=1)
               Output: t3.name, t3.n, 3
   ->  Sort  (cost=826.91..847.07 rows=8064 width=80) (actual time=0.410..0.429 rows=3 loops=1)
         Output: t1.name, t1.n, t2.name, t2.n, (1), (2), (COALESCE(t1.name, t2.name))
         Sort Key: (COALESCE(t1.name, t2.name))
         Sort Method: quicksort  Memory: 25kB
         ->  Merge Full Join  (cost=176.34..303.67 rows=8064 width=80) (actual time=0.176..0.254 rows=3 loops=1)
               Output: t1.name, t1.n, t2.name, t2.n, (1), (2), COALESCE(t1.name, t2.name)
               Merge Cond: (t1.name = t2.name)
               ->  Sort  (cost=88.17..91.35 rows=1270 width=40) (actual time=0.061..0.067 rows=1 loops=1)
                     Output: t1.name, t1.n, (1)
                     Sort Key: t1.name
                     Sort Method: quicksort  Memory: 25kB
                     ->  Seq Scan on public.t1  (cost=0.00..22.70 rows=1270 width=40) (actual time=0.014..0.021 rows=1 loops=1)
                           Output: t1.name, t1.n, 1
               ->  Sort  (cost=88.17..91.35 rows=1270 width=40) (actual time=0.089..0.110 rows=3 loops=1)
                     Output: t2.name, t2.n, (2)
                     Sort Key: t2.name
                     Sort Method: quicksort  Memory: 25kB
                     ->  Seq Scan on public.t2  (cost=0.00..22.70 rows=1270 width=40) (actual time=0.012..0.030 rows=3 loops=1)
                           Output: t2.name, t2.n, 2
 Planning time: 0.823 ms
 Execution time: 1.213 ms
(30 rows)



dbx=# SELECT * FROM
dbx-# (SELECT name, n as s1_n FROM t1) as s1
dbx-# NATURAL FULL JOIN
dbx-#   (SELECT * FROM
dbx(#     (SELECT name, n as s2_n, 2 as s2_2 FROM t2) as s2
dbx(#     NATURAL FULL JOIN
dbx(#     (SELECT name, n as s3_n FROM t3) as s3
dbx(#   ) ss2;
 name | s1_n | s2_n | s2_2 | s3_n 
------+------+------+------+------
 bb   |   11 |   12 |    2 |   13
 cc   |      |   22 |    2 |   23
 dd   |      |      |      |   33
 ee   |      |   42 |    2 |     
(4 rows)


                                                          QUERY PLAN                                                           
--------------------------------------------------------------------------------------------------------------------------------
 Merge Full Join  (cost=915.09..1689.53 rows=51206 width=48) (actual time=0.804..0.894 rows=4 loops=1)
   Output: COALESCE(t1.name, (COALESCE(t2.name, t3.name))), t1.n, t2.n, (2), t3.n
   Merge Cond: (t1.name = (COALESCE(t2.name, t3.name)))
   ->  Sort  (cost=88.17..91.35 rows=1270 width=36) (actual time=0.251..0.257 rows=1 loops=1)
         Output: t1.name, t1.n
         Sort Key: t1.name
         Sort Method: quicksort  Memory: 25kB
         ->  Seq Scan on public.t1  (cost=0.00..22.70 rows=1270 width=36) (actual time=0.186..0.193 rows=1 loops=1)
               Output: t1.name, t1.n
   ->  Sort  (cost=826.91..847.07 rows=8064 width=108) (actual time=0.526..0.551 rows=4 loops=1)
         Output: t2.n, t2.name, t3.n, t3.name, (COALESCE(t2.name, t3.name)), (2), (COALESCE(t2.name, t3.name))
         Sort Key: (COALESCE(t2.name, t3.name))
         Sort Method: quicksort  Memory: 25kB
         ->  Merge Full Join  (cost=176.34..303.67 rows=8064 width=108) (actual time=0.221..0.440 rows=4 loops=1)
               Output: t2.n, t2.name, t3.n, t3.name, COALESCE(t2.name, t3.name), (2), COALESCE(t2.name, t3.name)
               Merge Cond: (t2.name = t3.name)
               ->  Sort  (cost=88.17..91.35 rows=1270 width=40) (actual time=0.105..0.124 rows=3 loops=1)
                     Output: t2.n, t2.name, (2)
                     Sort Key: t2.name
                     Sort Method: quicksort  Memory: 25kB
                     ->  Seq Scan on public.t2  (cost=0.00..22.70 rows=1270 width=40) (actual time=0.016..0.037 rows=3 loops=1)
                           Output: t2.n, t2.name, 2
               ->  Sort  (cost=88.17..91.35 rows=1270 width=36) (actual time=0.088..0.109 rows=3 loops=1)
                     Output: t3.n, t3.name
                     Sort Key: t3.name
                     Sort Method: quicksort  Memory: 25kB
                     ->  Seq Scan on public.t3  (cost=0.00..22.70 rows=1270 width=36) (actual time=0.014..0.032 rows=3 loops=1)
                           Output: t3.n, t3.name
 Planning time: 0.794 ms
 Execution time: 1.294 ms
(30 rows)






select CONCAT(name, '(',left(occupation,1),')') from OCCUPATIONS order by name;
select concat('There are a total of ',count(*),' ',lower(occupation),'s.') from occupations group by occupation order by count(*), occupation asc;


select name from occupations order by occupation,name;

select name[0] from occupations where occupation='Doctor';




--Create a employee table
CREATE TABLE employees(
    id serial primary key,
    first_name varchar(40) NOT NULL,
    last_name varchar(40) NOT NULL);

--create a employee_audits table
--the table is used to save the last_name changed
CREATE TABLE employee_audits(
    id serial primary key,
    employee_id int4 NOT NULL,
    last_name varchar(40) NOT NULL,
    changed_on timestamp(6) NOT NULL
);


-- create a trigger function
CREATE OR REPLACE FUNCTION log_last_name_changes()
RETURNS trigger
LANGUAGE plpgsql AS
$$
BEGIN
    IF NEW.last_name <> OLD.last_name THEN
    INSERT INTO employee_audits(employee_id,last_name, changed_on)
    VALUES(OLD.id, OLD.last_name, now());
    END IF;
    RETURN NEW;
END;
$$;

-- create a trigger condition on table employees
CREATE TRIGGER last_name_changes
  BEFORE UPDATE
  ON employees
  FOR EACH ROW
  EXECUTE PROCEDURE log_last_name_changes();

-- Insert value into employees table
INSERT INTO employees (first_name, last_name) VALUES ('John', 'Doe');
INSERT INTO employees (first_name, last_name) VALUES ('Lily', 'Bush');

-- Check the content of the table employees
SELECT * FROM employees;

-- update the table by changing the last_name
UPDATE employees
SET last_name = 'Brown'
WHERE ID = 2;

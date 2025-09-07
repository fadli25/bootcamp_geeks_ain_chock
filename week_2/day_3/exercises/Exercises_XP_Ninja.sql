BEGIN;

-- Repartir propre
DROP TABLE IF EXISTS public.items;
DROP TABLE IF EXISTS public.customers;

-- Tables
CREATE TABLE public.items (
    id    integer PRIMARY KEY,
    name  text    NOT NULL,
    price integer NOT NULL CHECK (price >= 0)
);

CREATE TABLE public.customers (
    id         integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name  text NOT NULL
);

-- Données
INSERT INTO public.items (id, name, price) VALUES
 (1, 'Small Desk', 100),
 (2, 'Large Desk', 300),
 (3, 'Fan',        80);

INSERT INTO public.customers (id, first_name, last_name) VALUES
 (1, 'Greg',    'Jones'),
 (2, 'Sandra',  'Jones'),
 (3, 'Scott',   'Scott'),
 (4, 'Trevor',  'Green'),
 (5, 'Melanie', 'Johnson');

-- Requêtes demandées

-- 3.1 Tous les items
SELECT * FROM public.items ORDER BY id;

-- 3.2 Items avec un prix strictement > 80 (80 exclu)
SELECT * FROM public.items
WHERE price > 80
ORDER BY id;

-- 3.3 Items avec un prix <= 300 (300 inclus)
SELECT * FROM public.items
WHERE price <= 300
ORDER BY id;

-- 3.4 Clients dont le nom = 'Smith' (résultat attendu : 0 ligne)
SELECT * FROM public.customers
WHERE last_name = 'Smith';

-- 3.5 Clients dont le nom = 'Jones' (attendu : 2 lignes)
SELECT * FROM public.customers
WHERE last_name = 'Jones'
ORDER BY id;

-- 3.6 Clients dont le prénom n'est pas 'Scott' (attendu : 4 lignes)
SELECT * FROM public.customers
WHERE first_name <> 'Scott'
ORDER BY id;

COMMIT;




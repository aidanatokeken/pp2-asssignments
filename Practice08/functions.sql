CREATE OR REPLACE FUNCTION search_contacts(p TEXT)
RETURNS TABLE(name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT name, phone
    FROM contacts
    WHERE name ILIKE '%' || p || '%'
       OR phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, off INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, phone
    FROM contacts
    ORDER BY id
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE PROCEDURE add_phone(
    p_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE cid INT;
BEGIN
    SELECT id INTO cid FROM contacts WHERE name = p_name;

    IF cid IS NOT NULL THEN
        INSERT INTO phones(contact_id, phone, type)
        VALUES (cid, p_phone, p_type);
    END IF;
END;
$$;
CREATE OR REPLACE PROCEDURE move_to_group(
    p_name VARCHAR,
    p_group VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE gid INT;
BEGIN
    SELECT id INTO gid FROM groups WHERE name = p_group;

    IF gid IS NULL THEN
        INSERT INTO groups(name) VALUES (p_group)
        RETURNING id INTO gid;
    END IF;

    UPDATE contacts
    SET group_id = gid
    WHERE name = p_name;
END;
$$;
CREATE OR REPLACE FUNCTION search_contacts(p TEXT)
RETURNS TABLE(name TEXT, email TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, p2.phone
    FROM contacts c
    LEFT JOIN phones p2 ON c.id = p2.contact_id
    WHERE c.name ILIKE '%' || p || '%'
       OR c.email ILIKE '%' || p || '%'
       OR p2.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

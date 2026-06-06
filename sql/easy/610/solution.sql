select x,
       y,
       z,
       CASE WHEN (x + Y > Z) AND (x + Z > Y) AND (Y + z > X) THEN 'Yes' ELSE 'No' END AS triangle
from Triangle
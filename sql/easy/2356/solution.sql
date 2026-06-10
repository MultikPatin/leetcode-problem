select teacher_id, count(subject_id) as cnt
from Teacher
group by teacher_id

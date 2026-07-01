-- Write your query below
select left_operand, operator, right_operand,
    case 
        when operator = '>' and v1.value > v2.value then 'true'
        when operator = '<' and v1.value < v2.value then 'true'
        when operator = '=' and v1.value = v2.value then 'true'
        else 'false'
    end as value
from expressions join variables v1 on left_operand = v1.name join variables v2 on right_operand = v2.name;

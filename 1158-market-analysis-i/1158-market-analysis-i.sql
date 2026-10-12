# Write your MySQL query statement below
select
    u.user_id as buyer_id,
    u.join_date,
    count(o.order_id) orders_in_2019 
from users u
left join orders o
    on u.user_id = o.buyer_id
    and year(o.order_date) = 2019
group by u.user_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
-- 코드를 입력하세요
SELECT FH.FLAVOR
FROM FIRST_HALF FH
JOIN ICECREAM_INFO II
ON FH.FLAVOR = II.FLAVOR
WHERE FH.TOTAL_ORDER > 3000
AND II.INGREDIENT_TYPE = 'fruit_based'
ORDER BY FH.TOTAL_ORDER DESC;

# ✅ join 
# - 두 테이블이 있을 경우 해당 테이블을 합침.

# - 뭘 기준으로 합쳐야 되는지 필요하므로 그 때 같이 사용하는게 ON

 

# FROM 테이블A
# JOIN 테이블B
#   ON 테이블A.공통컬럼 = 테이블B.공통컬럼
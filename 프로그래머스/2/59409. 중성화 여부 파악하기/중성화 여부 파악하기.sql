# -- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
    CASE WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O' 
            WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O' 
            ELSE 'X'
    END AS SEX
FROM ANIMAL_INS;


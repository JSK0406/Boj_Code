-- 코드를 입력하세요
SELECT AUTHOR.AUTHOR_ID, AUTHOR.AUTHOR_NAME, BOOK.CATEGORY, SUM(BOOK.PRICE * BOOK_SALES.SALES) AS TOTAL_SALES
FROM BOOK
JOIN AUTHOR ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
JOIN BOOK_SALES ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
WHERE DATE_FORMAT(BOOK_SALES.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY AUTHOR_NAME, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC
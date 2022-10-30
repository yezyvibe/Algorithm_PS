SELECT C.party, count(C.party)
FROM Candidates C
RIGHT OUTER JOIN 
(SELECT R1.candidate_id
FROM (
    SELECT constituency_id, candidate_id, votes, ROW_NUMBER() 
    OVER (PARTITION BY constituency_id ORDER BY votes DESC) AS RankNo
    FROM Results) R1
WHERE RankNo = 1) R2
ON C.id = R2.candidate_id
GROUP BY C.party
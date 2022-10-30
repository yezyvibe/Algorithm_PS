function dfs(a, b, arr, N) {
  const dx = [-1, -1, -1, 0, 0, 1, 1, 1];
  const dy = [-1, 0, 1, -1, 1, -1, 0, 1];
  const visit = Array.from(Array(N + 1), () => new Array(N + 1).fill(0));
  let stack = [[a, b]];
  visit[a][b] = 1;

  while (stack.length > 0) {
    const [x, y] = stack.pop();
    for (let i = 0; i < 8; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (0 <= nx && nx < N + 1 && 0 <= ny && ny < N + 1) {
        if (visit[nx][ny] === 0) {
          // 방문하지 않았으면 방문 처리
          visit[nx][ny] = 1;
          arr[nx][ny] === 0 ? stack.push([nx, ny]) : "";
        }
      }
    }
  }
  let answer = 0;
  visit.forEach((el) => {
    answer += el.reduce((a, b) => a + b, 0);
  });
  return answer;
}

function solution(N, mine, P) {
  // 이차원 배열 만들기
  const arr = Array.from(Array(N + 1), () => new Array(N + 1).fill(0));

  // 지뢰 심기
  mine.forEach((el) => {
    const [a, b] = el;
    arr[a][b] = "@";
  });
  // 숫자 넣기
  const dx = [-1, -1, -1, 0, 0, 1, 1, 1];
  const dy = [-1, 0, 1, -1, 1, -1, 0, 1];

  for (let i = 0; i < N + 1; i++) {
    for (let j = 0; j < N + 1; j++) {
      let cnt = 0;
      for (let k = 0; k < 9; k++) {
        if (arr[i][j] === "@") break;
        let nx = i + dx[k];
        let ny = j + dy[k];
        if (0 <= nx && nx < N + 1 && 0 <= ny && ny < N + 1) {
          if (arr[nx][ny] === "@") {
            cnt++;
          }
        }
      }
      if (arr[i][j] === "@") {
        continue;
      }
      cnt > 0 ? (arr[i][j] = cnt) : "";
    }
  }
  return dfs(P[0], P[1], arr, N);
}

const N = 9;
const mine = [
  [1, 2],
  [2, 6],
  [3, 4],
  [3, 8],
  [4, 9],
  [5, 4],
  [5, 8],
  [6, 7],
  [7, 2],
  [9, 1],
];
const P = [8, 5];
console.log(solution(N, mine, P));

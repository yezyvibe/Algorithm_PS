function solution(src) {
  let answer = "";
  let tmpChar = "";
  let cnt = 0;
  src += "@";
  for (let i = 0; i < src.length; i++) {
    if (tmpChar === "") {
      answer += src[i];
      tmpChar = src[i];
      cnt++;
    } else if (tmpChar === src[i]) {
      cnt++;
    } else if (tmpChar !== src[i]) {
      answer += String.fromCharCode(cnt + 64);
      cnt = 1;
      tmpChar = src[i];
    }
  }
  return answer;
}

const src = "111100100011";
console.log(solution(src));

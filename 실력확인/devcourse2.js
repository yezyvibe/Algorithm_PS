function solution(n, queries) {
  const IP_PREFIX = "192.168.0.";
  let answer = [];
  // 1. 할당되지 않은 ip 배열
  let unassingedIp = [];
  for (let i = 1; i <= n; i++) {
    unassingedIp.push(i);
  }
  // 2. 할당된적 있고 현재 사용중이지 않은 ip 배열
  let usableIp = [];

  // 각 컴퓨터마다 현재 사용중인 ip, 또는 사용했었던 ip 목록
  let computerDict = {};

  function searchIp(computer, answer) {
    if (unassingedIp.length > 0) {
      let currentIp = unassingedIp.shift();
      computerDict[computer].push(currentIp);
      answer.push([computer, IP_PREFIX + currentIp].join(" "));
    } else if (usableIp.length > 0) {
      usableIp.sort();
      let currentIp = usableIp.shift();
      computerDict[computer].push(currentIp);
      answer.push([computer, IP_PREFIX + currentIp].join(" "));
    } else {
      // 모두 사용 불가능 -> 요청 거부
      answer.push([computer, "reject"].join(" "));
    }
    return answer;
  }

  queries.forEach((query) => {
    let [computer, ask] = query.split(" ");
    if (ask === "request") {
      if (computer in computerDict) {
        // 이미 할당 받은 적이 있음
        let ipArray = computerDict[computer];
        let recentIp = ipArray[ipArray.length - 1];
        if (usableIp.indexOf(recentIp) !== -1) {
          // 가장 최근 ip가 사용 가능한 경우
          usableIp = usableIp.filter((el) => el !== recentIp);
          answer.push([computer, IP_PREFIX + recentIp].join(" "));
        } else {
          // 가장 최근 ip 사용 불가능
          answer = searchIp(computer, answer);
        }
      } else {
        // 처음 할당 받는 컴퓨터
        computerDict[computer] = [];
        answer = searchIp(computer, answer);
      }
    } else {
      // 반납인 경우
      let ipArray = computerDict[computer];
      let recentIp = ipArray[ipArray.length - 1];
      usableIp.push(recentIp);
    }
  });
  return answer;
}

let n = 2;
let queries = [
  "desktop1 request",
  "desktop2 request",
  "desktop1 release",
  "desktop2 release",
  "desktop3 request",
  "desktop3 release",
  "desktop2 request",
  "desktop1 request",
];

console.log(solution(n, queries));

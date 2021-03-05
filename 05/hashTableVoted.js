const voted = {};

const value = voted.hasOwnProperty("tom");
console.log(value); // "tom"이라는 property가 없으므로 false를 내놓는다.

const check_voter = (name) => {
	if (voted.hasOwnProperty(name)) {
		console.log("쫓아내세요!");
	} else {
		voted[name] = true;
		console.log("투표하게 하세요.");
	}
};

check_voter("tom");
console.log(voted);
check_voter("mike");
console.log(voted);
check_voter("mike"); // 이미 voted 안에 mike가 존재하므로 "쫓아내세요!"가 출력된다.

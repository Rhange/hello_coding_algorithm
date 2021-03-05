const cache = {};

const get_page = (url) => {
	// 만약 cache object 안에 해당 url을 property 값으로 가지고 있으면
	// property 값에 해당하는 value를 리턴한다.
	if (cache.hasOwnProperty(url)) {
		return cache[url];
	} else {
		// 그렇지 않다면 해당 url에 해당하는 데이터를 받아와서
		// cache object에 새롭게 추가하고 해당 데이터를 리턴한다.
		const data = get_data_from_server(url);
		cache[url] = data;
		return data;
	}
};

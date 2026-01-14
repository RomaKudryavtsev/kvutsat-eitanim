export async function baseFetch(endpoint, options = {}) {
    const url = `/api/${endpoint}`;
    const response = await fetch(url, {
        headers: {
            'Content-Type': 'application/json',
            ...options.headers,
        },
        ...options
    });
    console.log('Fetch URL:', url);
    const data = await response.json();
    console.log('Fetch response:', data);
    if (!response.ok) {
        throw new Error(data.error || data.message || `HTTP error! status: ${response.status}`);
    }
    return data;
}
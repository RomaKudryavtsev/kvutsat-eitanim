import { NextResponse } from 'next/server';
import { revalidateTag } from 'next/cache';

export async function POST(request) {
    try {
        const body = await request.json();
        const { tags } = body;
        if (!tags || !Array.isArray(tags) || tags.length === 0) {
            return NextResponse.json({ error: 'Missing tag' }, { status: 400 });
        }
        console.log('Revalidation signal for tags: ', tags)
        for (const tag of tags) {
            revalidateTag(tag);
        }
        return NextResponse.json({ revalidated: true, tags });
    } catch (error) {
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
}
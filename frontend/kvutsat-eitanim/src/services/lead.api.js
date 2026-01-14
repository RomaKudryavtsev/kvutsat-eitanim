import { baseFetch } from "./base.service";

export async function submitLead(leadData) {
    return await baseFetch('lead', {
        method: 'POST',
        body: JSON.stringify(leadData),
    });
}
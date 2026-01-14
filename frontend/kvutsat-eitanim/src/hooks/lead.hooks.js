import { useMutation } from "@tanstack/react-query";
import { submitLead } from "@/services/lead.service";

export function useSubmitLead() {
    return useMutation({
        mutationFn: async (leadData) => {
            return await submitLead(leadData);
        },
    });
}
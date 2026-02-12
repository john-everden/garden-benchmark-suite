
### {{ID}}
***Question: {{QUESTION-PROMPT}}***
{{#if CONTEXT-BLOCK}}
**Context:**  
{{CONTEXT-BLOCK}}
{{/if}}
{{#if (eq TYPE "MULTIPLE-CHOICE")}}
**Choices:**
{{#each MULTIPLE-CHOICE-ANSWERS}}
- **{{LETTER}}:** {{ANSWER}}
{{/each}} 
{{/if}}

**Your Answer{{#if (eq TYPE "MULTIPLE-CHOICE")}} (letter){{/if}}:❓**

---


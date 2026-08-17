	1. Being specific about the exact scenarios and format gave a much more usable output. 
	Example - "Write a test case for a login page." Read the response. Then, in a new message, 
	type: "Write a test case for a login page that checks: empty username, wrong password, 
	SQL injection attempt, and account lockout after 5 failed tries. Format as a table with 
	columns: Test Case, Steps, Expected Result."
	
	2. Providing examples help in retrieving the output in the format that is relevant to your 
	work/ organization and much more accurate. Example - Provide samples of your bug reports 
	and then ask the LLM to write another bug report.
	
	3. When you ask the model to think through the steps first, you get a much more comprehensive
	explanation of why we should do something, not just what to do. You get reasoning + tradeoffs + context 
	→ better decision-making. Example - hould we test this feature manually or automate it —
	a one-time internal admin tool used by 3 people?
	
	4. Using structured tags in your prompts makes output more scannable, extractable, and reusable 
	than unstructured prose. When you need reusability and clarity structure beats prose. 
	Example - Put the summary in <summary> tags and the test cases in <test_cases> tags.

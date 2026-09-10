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

	--------------------------------------------------------------------------------------------------
	Why does AI Assertion matters for testing dynamic content?
	- Traditional assertions require an exact string match so they break the moment wording changes even slightly.
	Ex: if a product team A/B tests different confirmation copy, translates the site or the content itself becomes
	AI generated and varies each time. A semantic/LLM based assertion confirms if the message correctly confirms the order,
	so it keeps working correctly regardless of exact phrasing, as long as the underlying meaning is right. This matters 
	increasingly for real-world testing, since more UI content (chatbot responses, personalized messages, AI-generated summaries)
	is dynamic by design rather than fixed text

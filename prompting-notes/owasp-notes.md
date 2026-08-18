OWASP - open worldwide application security project
10 threats - 
	1. Prompt Injection - 
  untrusted input alters model behavior due to no architectural distinction between instructions and data.
  Example - An attacker prompts a customer-support chatbot to ignore its guidelines, query private data 
  stores and send emails leading to unauthorized access and privilege escalation.
  
	2. Sensitive information disclosure-
  Exposure of propriety data, sensitive data, confidential, regulated and privileged data. 
  Example - Prompt injection makes a support bot print its system prompt and an embedded vendor API key.
  
	3. Excessive agency - 
  granting models excessive permissions, autonomy or unsafe tool access, allowing 
  compromised outputs to execute unintended actions. 
  Example - hijacked email assistant. LLM based personal assistants tool selected by developer, contains
  functions for sending messages  
  
	4. Supply Chain - 
  Vulnerabilities in third party datasets, pre-trained models, plugins, tools integrations or fine-tuning artifacts.
  Example - Reverse engineered mobile app - an attacker reverse engineers a mobile app to replace the on-device model 
  with a tampered version that leads to scam site, distributing the re-packaged app through social engineering.
  
	5. Data and Model poisoning - 
  manipulation of training data, RAG stores, or fine tuning pipelines to introduce backdoors, biases or security weaknesses.
  Example - An attacker inserts manipulated documents into an internal knowledge repository. Poisoned documents surface 
  in responses leading to incorrect recommendations.
  
	6. Unbounded consumption - 
  Resource exhaustion caused by uncontrolled inputs, complex queries, or looping agent calls. 
  Example - An unusually large input to an LLM application that processes text data, resulting in excessive memory usage 
  and CPU load, crashing system or slowing down service.
  
	7. Misinformation - 
  Fluent but hallucinatory output that drive erroneous downstream  actions or decision-making. 
  Example - False Alert triggers automated response - A security agent misclassifies normal traffic as an intrusion and 
  automatically blocks a production network, segment causing an outage
  
	8. Hidden Context Exposure - 
  Failure to protect sensitive instructions, systems prompts or hidden context frames from user inspection or manipulation. 
  Example - LLM has a system prompt that contains a set of credentials used for a tool that it has been given access to. 
  System prompt is leaked to an attacker who is able to use these credentials for other purposes.
  
	9. Vector and Embedding Weaknesses - Security flaws in vector databases, embedding generation, or retrieval mechanisms 
  enabling unauthorized data access or retrieval poisoning. 
  Example - A company's RAG system scrapes public documentation and forum posts on a schedule. An attacker publishes posts
  engineered so their embeddings land near specific internal queries, such as "what is our Q3 revenue projection." When an
  employee asks that question, the attacker's content is retrieved and fed to the LLM. The same text pasted into a chat would
  have no effect. The attack works only because the attacker can place content near a target query in embedding space.
  
	10. Improper Output Handling - 
  Insufficient validation, sanitization, or filtering of model outputs before passing them to interpreters, shell, browsers, or 
  downstream applications. 
  Example - An application automatically compiles and deploys LLM-generated code without human review or security testing. 
  Because the output is trusted and executed without validation, insecure code reaches production and is exploited.

"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

# region imports
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent

llm = ChatOpenAI(model='gpt-4o')
# agent = Agent(
# 	task='Go to https://eportal.incometax.gov.in/iec/foservices/#/login. Login with the following credentials: username: biqpm4787b, password: India@320 and Download the ITR form for year 2024-25',
# 	llm=llm,
# )
agent = Agent(
    task= 'Go to https://dev-tgpt.trustt.com/chatbot/ and test the chatbot flow. At start give theMy mobile number is 9014142377 and otp is 781345. Loan Amount is 50000 and Tenure is 12 months. Handle other prompts as well.',
    llm=llm,
)


async def main():
	await agent.run(max_steps=20)
	input('Press Enter to continue...')


asyncio.run(main())
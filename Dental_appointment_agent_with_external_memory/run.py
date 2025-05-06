import asyncio

config = {
    "configurable": {
        "thread_id": "2"
    }
}

initial_state = {
    "messages": [
        HumanMessage(content="Book an appointment for 2 days later for Dental Checkup")
    ]
}

async def run_workflow():
    print("📤 Starting the appointment scheduling flow...\n")
    async for chunk in app.astream(initial_state, config=config, stream_mode="values"):
        response_message = chunk["messages"][-1]
        if hasattr(response_message, 'content'):
            response_message.pretty_print()

        else:
            print("⚠️ Received a message without a 'content' attribute.")

await run_workflow()
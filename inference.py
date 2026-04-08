import asyncio
from env import HostelEnv

async def main():
    env = HostelEnv()

    # START
    print("[START] task=hostel env=custom model=rule-based", flush=True)

    rewards = []
    steps = 0

    state = env.reset()   # ✅ NO await

    done = False

    while not done and steps < 5:
        steps += 1

        # Simple logic
        action = {
            "category": "Cleaning",
            "priority": "High"
        }

        result = env.step(action)   # ✅ NO await

        reward = result.get("reward", 0.0)
        done = result.get("done", False)

        rewards.append(reward)

        print(
            f"[STEP] step={steps} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
            flush=True
        )

    score = sum(rewards)
    success = score > 0

    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={','.join([f'{r:.2f}' for r in rewards])}",
        flush=True
    )

if __name__ == "__main__":
    asyncio.run(main())
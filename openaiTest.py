import openai

# 初始化API密钥
openai.api_key = "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"

def interact_with_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def Test():
    # 自动生成游戏背景和世界观
    world_prompt = "在一个中世纪奇幻世界中，玩家需要拯救被邪恶势力控制的国度。"
    world_setting = interact_with_chatgpt(world_prompt)

    # 自动生成NPC互动文本和剧情
    npc_prompt = f"在{world_setting}的背景下，为一个矮人铁匠生成一个关于寻找失落宝物的支线任务。"
    npc_interaction_and_plot = interact_with_chatgpt(npc_prompt)

    # 输出生成的游戏背景、世界观和NPC互动文本及剧情
    print("[游戏背景和世界观]：", world_setting)
    print("[NPC互动文本和剧情]：", npc_interaction_and_plot)

if __name__ == "__main__":
    Test()

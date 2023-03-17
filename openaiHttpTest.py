import openai
import json

openai.api_key = "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"

import json

def interact_with_chatgpt(messages, model="gpt-3.5-turbo"):
    """
    与ChatGPT进行交互，并获取响应。
    :param messages: 一个包含指示和问题的列表。
    :param model: 使用的模型名称，默认为"gpt-3.5-turbo"。
    :return: 从ChatGPT返回的生成文本。
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    generated_text = response['choices'][0]['message']['content']
    return generated_text

def generate_game_content(npc_count, npc_interactions, keywords):
    """
    自动生成游戏内容。
    :param npc_count: 生成的NPC数量。
    :param npc_interactions: 每个NPC之间的交互次数。
    :param keywords: 世界观和背景的关键词。
    :return: 自动生成的游戏内容。
    """

    # 初始化消息列表
    messages = [
        {
            "role": "system",
            "content": "你是一个用于生成游戏剧情世界观交互文本的生成器。"
        },
        {
            "role": "user",
            "content": f"根据关键词：{keywords}，生成游戏的基本背景和世界观。"
        }
    ]

    # 生成游戏背景和世界观
    game_world = interact_with_chatgpt(messages)
    game_content = {'game_world': game_world, 'npcs': []}

    game_npcs = "";
    # 自动生成NPC角色和互动
    for i in range(npc_count):
        messages[-1]['content'] = f"根据世界观{game_content['game_world']},生成第{i + 1}个NPC的角色、性格、背景故事和动机。"
        npc = interact_with_chatgpt(messages)
        game_npcs += npc + "、"

        interactions = []
        for j in range(npc_interactions):
            messages[-1]['content'] = f"根据世界观{game_content['game_world']}和这些npc{game_npcs},为第{i + 1}个NPC生成第{j + 1}个互动。"
            interaction = interact_with_chatgpt(messages)
            interactions.append(interaction)

        game_content['npcs'].append({'npc': npc, 'interactions': interactions})

    return game_content

npc_count = 5
npc_interactions = 5
keywords = "中世纪奇幻世界"

game_content = generate_game_content(npc_count, npc_interactions, keywords)
print(json.dumps(game_content, indent=2, ensure_ascii=False))

from utils.groq_client import call_groq_llm
from utils.helpers import load_text, save_text, safe_call_llm, count_tokens


def summary_text(summary_type: str, chunks, debug_save=True):
    if not chunks:
        raise ValueError("Chunks list is empty")

    if summary_type == "bullet":
        prompt_template = load_text("./prompts/bullet.txt")
    elif summary_type == "detailed":
        prompt_template = load_text("./prompts/detailed.txt")
    elif summary_type == "executive":
        prompt_template = load_text("./prompts/executive.txt")
    else:
        raise ValueError(f"Unknown summary type: {summary_type}")

    client = call_groq_llm()
    total_tokens_all = 0

    if len(chunks) == 1:
        final_summary = safe_call_llm(client, f"{prompt_template}\n\n{chunks[0]}")
        tokens_input = count_tokens(f"{prompt_template}\n\n{chunks[0]}")
        tokens_output = count_tokens(final_summary)
        total_tokens_all += tokens_input + tokens_output
        print(f"Batch 1 - Input tokens: {tokens_input}, Output tokens: {tokens_output}")
    else:
        # batch summary → gabung per GROUP_SIZE
        batch_summaries = []
        GROUP_SIZE = 3
        for i in range(0, len(chunks), GROUP_SIZE):
            batch_text = "\n\n".join(chunks[i : i + GROUP_SIZE])
            prompt = f"{prompt_template}\n\n{batch_text}"
            batch_summary = safe_call_llm(client, prompt)
            batch_summaries.append(batch_summary)

            # hitung token input + output per batch
            tokens_input = count_tokens(prompt)
            tokens_output = count_tokens(batch_summary)
            total_tokens_all += tokens_input + tokens_output
            print(
                f"Batch {i // GROUP_SIZE + 1} - Input tokens: {tokens_input}, Output tokens: {tokens_output}"
            )

        # gabungkan semua batch summary → tanpa panggilan tambahan
        final_summary = "\n\n".join(batch_summaries)

    print(f"Total estimated tokens (input + output): {total_tokens_all}")

    if debug_save:
        save_text("./outputs/4_summaries/output.txt", final_summary)

    return final_summary

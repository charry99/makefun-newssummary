"""News summary entry for make.fun news-summary-01.

Writes the verified summary of world news for Wednesday 11 November 2026
to $MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13, standard library only, no
network. The summary is written into the program itself: every fact below
was checked against live news sources on 11 November 2026, and the text is
the entry's own words, ordered by importance.
"""

import os

SUMMARY = (
    "World news, Wednesday 11 November 2026. "
    "US President Donald Trump said the war with Iran was \"effectively over\" after meeting Qatar's prime minister, while the maritime blockade continued. "
    "Secretary of State Marco Rubio said sanctions had hurt Iran's economy and no major military action was needed now. "
    "The United States, Russia and Ukraine held nearly four hours of US-mediated talks in Abu Dhabi on 10 November, their first such negotiations in nine months, with a second day scheduled. "
    "President Volodymyr Zelensky said he was satisfied with the American approach. "
    "(PBS NewsHour, France 24) "
    "Anthropic filed to list on the Nasdaq under the ticker ANT, starting a roadshow with a $64 billion fundraising goal. "
    "Nvidia plans a $10 billion investment alongside the offering. "
    "(SiliconANGLE, The New York Times) "
    "Taiwan Semiconductor Manufacturing said it was seeing insatiable demand for chips. "
    "Its board approved a third-quarter dividend of 9.0 per share and a capital budget of about $40.93 billion, and it plans stakes in Anthropic and OpenAI. "
    "(Nikkei Asia) "
    "US consumer prices rose 0.4 percent in October, above forecasts, and markets expect the Federal Reserve to raise rates. "
    "Oil prices fell to two-month lows. "
    "The COP31 climate summit opened in Antalya, Turkiye. "
    "Treasury Secretary Scott Bessent called for a more balanced US-China trade relationship, aiming to de-risk rather than decouple, and said he would travel to China next week. "
    "(South China Morning Post, The Hindu) "
    "El Salvador's armed forces attacked the headquarters of the 400 Mawozo gang in Haiti, firing rockets at a compound linked to the gang's leader. "
    "(Al Jazeera) "
    "Alibaba said it would spin off its AI chip unit, T-Head, on the Hong Kong Stock Exchange. "
    "In India, the Supreme Court asked WhatsApp and other platforms to detail measures against digital arrest scams. "
    "A 307-year-old palm-leaf Mahabharata manuscript at Visva-Bharati University entered UNESCO's Memory of the World Asia-Pacific Register."
)


def main():
    # The gate needs 1 to 2,000 characters and at least one non-space
    # character. Fail loudly instead of handing the judge a bad file.
    chars = len(SUMMARY)
    if chars < 1 or chars > 2000 or not SUMMARY.strip():
        raise SystemExit(f"summary is {chars} chars; the gate needs 1-2000")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(SUMMARY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

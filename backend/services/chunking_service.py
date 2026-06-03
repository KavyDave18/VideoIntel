MIN_WORDS = 200
TARGET_WORDS = 250
MAX_WORDS = 350


def create_chunks(segments):

    chunks = []

    current_segments = []
    current_word_count = 0

    chunk_index = 0

    for segment in segments:

        segment_text = segment.text.strip()

        if not segment_text:
            continue

        current_segments.append(segment)

        current_word_count += len(segment_text.split())

        sentence_boundary = (
            segment_text.endswith(".")
            or segment_text.endswith("?")
            or segment_text.endswith("!")
        )

        # Ideal chunk
        if (
            TARGET_WORDS <= current_word_count <= MAX_WORDS
            and sentence_boundary
        ):

            chunk_text = " ".join(
                seg.text.strip()
                for seg in current_segments
            )

            chunks.append(
                {
                    "chunk_index": chunk_index,
                    "start_time": current_segments[0].start_time,
                    "end_time": current_segments[-1].end_time,
                    "word_count": current_word_count,
                    "chunk_text": chunk_text
                }
            )

            chunk_index += 1

            current_segments = []
            current_word_count = 0

        # Safety cutoff
        elif current_word_count > MAX_WORDS:

            chunk_text = " ".join(
                seg.text.strip()
                for seg in current_segments
            )

            chunks.append(
                {
                    "chunk_index": chunk_index,
                    "start_time": current_segments[0].start_time,
                    "end_time": current_segments[-1].end_time,
                    "word_count": current_word_count,
                    "chunk_text": chunk_text
                }
            )

            chunk_index += 1

            current_segments = []
            current_word_count = 0

    # Remaining segments
    if current_segments:

        chunk_text = " ".join(
            seg.text.strip()
            for seg in current_segments
        )

        chunks.append(
            {
                "chunk_index": chunk_index,
                "start_time": current_segments[0].start_time,
                "end_time": current_segments[-1].end_time,
                "word_count": current_word_count,
                "chunk_text": chunk_text
            }
        )

    return chunks
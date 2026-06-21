import psycopg2

print("LOADED FUNCTIONS FROM:", __file__)

def get_connection():

    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="wordis",
            user="postgres",
            password="lietuva"
        )

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        conn = None

    if conn:
        print("Connected!")

        return conn


def insert_verb(
    infinitive,
    stem,
    translation_en,

    present_as,
    present_tu,
    present_jis_ji,
    present_mes,
    present_jus,
    present_jie_jos,

    past_as,
    past_tu,
    past_jis_ji,
    past_mes,
    past_jus,
    past_jie_jos,

    future_as,
    future_tu,
    future_jis_ji,
    future_mes,
    future_jus,
    future_jie_jos,

    sample_1_lt,
    sample_1_en,

    sample_2_lt,
    sample_2_en,

    sample_3_lt,
    sample_3_en,

    image_url=None
):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO verbs (

            infinitive,
            stem,
            translation_en,

            image_url,

            present_as,
            present_tu,
            present_jis_ji,
            present_mes,
            present_jus,
            present_jie_jos,

            past_as,
            past_tu,
            past_jis_ji,
            past_mes,
            past_jus,
            past_jie_jos,

            future_as,
            future_tu,
            future_jis_ji,
            future_mes,
            future_jus,
            future_jie_jos,

            sample_1_lt,
            sample_1_en,

            sample_2_lt,
            sample_2_en,

            sample_3_lt,
            sample_3_en

        )

        VALUES (

            %s, %s, %s,

            %s,

            %s, %s, %s, %s, %s, %s,

            %s, %s, %s, %s, %s, %s,

            %s, %s, %s, %s, %s, %s,

            %s, %s,

            %s, %s,

            %s, %s
        )
    """, (

        infinitive,
        stem,
        translation_en,

        image_url,

        present_as,
        present_tu,
        present_jis_ji,
        present_mes,
        present_jus,
        present_jie_jos,

        past_as,
        past_tu,
        past_jis_ji,
        past_mes,
        past_jus,
        past_jie_jos,

        future_as,
        future_tu,
        future_jis_ji,
        future_mes,
        future_jus,
        future_jie_jos,

        sample_1_lt,
        sample_1_en,

        sample_2_lt,
        sample_2_en,

        sample_3_lt,
        sample_3_en
    ))

    conn.commit()

    print("VERB INSERTED!")

    cur.close()
    conn.close()

if __name__ == "__main__":
    # test code only here
    get_connection()
    insert_verb()
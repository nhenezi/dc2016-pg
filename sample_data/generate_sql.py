import random
import string
import datetime

MIN_PEOPLE = 5 * 1000 * 1000

MIN_POSTS = 15 * 1000 * 1000
MIN_THREADS = 6 * 1000 * 1000
MIN_TAG_TYPE = 1000
MIN_TAGS = 8 * 1000 * 1000

# Iteration values
PEOPLE_PER_ITERATION = 1000
MIN_POSTS_ITERATION_SIZE = 1000
MAX_POSTS_ITERATION_SIZE = 5000

MIN_TAGS_ITERATION_SIZE = 1000
MAX_TAGS_ITERATION_SIZE = 5000

MIN_THREADS_ITERATION_SIZE = 1000
MAX_THREADS_ITERATION_SIZE = 5000

def random_date():
    return datetime.datetime(random.randint(2000, 2016),
                             random.randint(1, 12),
                             random.randint(1, 28),
                             random.randint(0, 23),
                             random.randint(0, 59),
                             random.randint(0, 59)
    )


def random_location():
    return "(%s,%s)" % (random.uniform(-180, 180), random.uniform(-180, 180))


def random_key():
    key_length = random.choice([i for i in xrange(15, 20)])
    return ''.join(
        random.choice(string.lowercase) for _ in xrange(key_length)
    )


def generate_tag_types(outfile='tag_types.csv'):
    tag_type_out = open(outfile, 'w')
    tag_type_id = 1

    while tag_type_id < MIN_TAG_TYPE:
        tag_type_out.write(tag_type_csv(tag_type_id) + "\n")
        tag_type_id += 1


def generate_tags(outfile='tags.csv'):
    tag_out = open(outfile, 'w')
    tag_id = 1
    while tag_id < MIN_TAGS:
        tag_data = ""
        posts = random.sample(
            xrange(MIN_PEOPLE),
            random.randint(MIN_TAGS_ITERATION_SIZE, MAX_TAGS_ITERATION_SIZE)
        )
        dates = [random_date() for _ in xrange(len(posts))]

        cnt = 0
        for p in posts:
            tag_data += tag_csv(tag_id, p, dates[cnt]) + "\n"
            cnt += 1
            tag_id += 1
        print tag_id
        tag_out.write(tag_data)


def generate_posts(outfile='posts.csv'):
    post_out = open(outfile, 'w')
    post_id = 1
    while post_id < MIN_POSTS:
        post_data = ""
        users = random.sample(
            xrange(MIN_PEOPLE),
            random.randint(MIN_POSTS_ITERATION_SIZE, MAX_POSTS_ITERATION_SIZE)
        )
        dates = [random_date() for _ in xrange(len(users))]

        threads = random.sample(
            xrange(MIN_THREADS),
            len(users)
        )

        sponsored = 8 < random.randint(0, 10)
        cnt = 0
        for u in users:
            post_data += post_csv(post_id, u, threads[cnt], sponsored, dates[cnt]) + "\n"
            cnt += 1
            post_id += 1
        print post_id
        post_out.write(post_data)

def generate_threads(outfile='threads.csv'):
    thread_out = open(outfile, 'w')
    thread_id = 1
    while thread_id < MIN_THREADS:
        thread_data = ""
        users = random.sample(
            xrange(MIN_PEOPLE),
            random.randint(MIN_THREADS_ITERATION_SIZE, MAX_THREADS_ITERATION_SIZE)
        )
        dates = [random_date() for _ in xrange(len(users))]

        sticky = 9 < random.randint(0, 1)

        cnt = 0
        for u in users:
            thread_data += thread_csv(thread_id, u, sticky, dates[cnt]) + "\n"
            cnt += 1
            thread_id += 1
        print thread_id
        thread_out.write(thread_data)



def generate_users(outfile='users.csv'):
    male = [m.strip().capitalize() for m in open('male_first.txt', 'r').readlines()]
    female = [f.strip().capitalize() for f in open('female_first.txt', 'r').readlines()]
    last = [l.strip().capitalize() for l in open('last.txt', 'r').readlines()]
    users_out = open(outfile, 'w')

    print "done"
    for i in xrange(int(MIN_PEOPLE/(PEOPLE_PER_ITERATION * 2))):
        user_data = ""
        male_choice = random.sample(male, PEOPLE_PER_ITERATION)
        female_choice = random.sample(female, PEOPLE_PER_ITERATION)
        last_choice = random.sample(last, PEOPLE_PER_ITERATION * 2)
        keys = [random_key() for _  in xrange(PEOPLE_PER_ITERATION * 2)]
        locations = [random_location() for _ in xrange(PEOPLE_PER_ITERATION * 2)]
        dates = [random_date() for _ in xrange(PEOPLE_PER_ITERATION * 2)]

        for s in xrange(PEOPLE_PER_ITERATION):
            user_data += person_csv(
                2 * i * PEOPLE_PER_ITERATION + s*2,
                male_choice[s],
                last_choice[s*2],
                "Male",
                keys[s*2],
                locations[s*2],
                dates[s*2]) + "\n"

            user_data += person_csv(
                2 * i * PEOPLE_PER_ITERATION + s*2 + 1,
                female_choice[s],
                last_choice[s*2 + 1],
                "Female",
                keys[s*2+1],
                locations[s*2+1],
                dates[s*2+1]) + "\n"
        print i * PEOPLE_PER_ITERATION
        users_out.write(user_data)


def person_csv(id, first_name, last_name, sex, referal, last_location, date):
    return '%s,%s,%s,%s,%s,"%s","%s"' % (id, first_name, last_name, sex,
                                         referal, last_location, date)


def thread_csv(id, author_id, sticky, created):
    return '%s,%s,%s,"%s"' % (id, author_id, sticky, created)


def post_csv(id, person_id, thread_id, sponsored, time):
    return '%s,%s,%s,%s,"%s"' % (id, person_id, thread_id, sponsored, time)


def tag_csv(post_id, tag_id, created):
    return '%s,%s,"%s"' % (post_id, tag_id, created)


def tag_type_csv(id):
    return '%s' % (id)


def generate_all():
    generate_tag_types()
    generate_tags()
    generate_threads()
    generate_users()
    generate_posts()

if __name__ == '__main__':
    generate_all()

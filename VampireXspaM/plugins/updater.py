import asyncio
import os
import sys
import git
from telethon import events
from .. import Don, Don2, Don3, Don4, Don5, Don6, Don7, Don8, Don9, Don10, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY


# -- Constants -- #
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)
OFFICIAL_UPSTREAM_REPO = "https://github.com/don1900/TeamAlwaysSpam"
BOT_IS_UP_TO_DATE = "**Don Rocketsð** is up-to-date bochlike."
NEW_BOT_UP_DATE_FOUND = (
    "new update found for {branch_name}\n"
    "changelog: \n\n{changelog}\n"
    "updating your Gunð ..."
)
NEW_UP_DATE_FOUND = "New update found for {branch_name}\n" "`updating your Don Rockets ð..`"
REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
DIFF_MARKER = "HEAD..{remote_name}/{branch_name}"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? ð "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
# -- Constants End -- #

@Don.on(events.NewMessage(pattern=".update"))
@Don2.on(events.NewMessage(pattern=".update"))
@Don3.on(events.NewMessage(pattern=".update"))
@Don4.on(events.NewMessage(pattern=".update"))
@Don5.on(events.NewMessage(pattern=".update"))
@Don6.on(events.NewMessage(pattern=".update"))
@Don7.on(events.NewMessage(pattern=".update"))
@Don8.on(events.NewMessage(pattern=".update"))
@Don9.on(events.NewMessage(pattern=".update"))
@Don10.on(events.NewMessage(pattern=".update"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "__Uð½ð±ð®ðð¶ð»ð´..... ð¦ð½ð®ðº ð¨ðð²ð¿ð¯ð¼ðð__\nð§ðð½ð² .ping ðð³ðð²ð¿ 5ðºð¶ð»ð ð§ð¼ ð°ðµð²ð°ð¸ ð'ðº ð¼ð» !!"
        await e.reply(text, parse_mode=None, link_preview=None)



@Don.on(
    events.NewMessage(pattern="^.update", func=lambda e: e.sender_id in SUDO_USERS)
)
async def updater(message):
    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(IFFUCI_ACTIVE_BRANCH_NAME, origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != IFFUCI_ACTIVE_BRANCH_NAME:
        await message.edit(
            IS_SELECTED_DIFFERENT_BRANCH.format(branch_name=active_branch_name)
        )
        return False

    try:
        repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
    except Exception as e:
        print(e)

    temp_upstream_remote = repo.remote(REPO_REMOTE_NAME)
    temp_upstream_remote.fetch(active_branch_name)

    changelog = generate_change_log(
        repo,
        DIFF_MARKER.format(
            remote_name=REPO_REMOTE_NAME, branch_name=active_branch_name
        ),
    )

    if not changelog:
        await message.edit("`Updation in Progress......`")
        await asyncio.sleep(5)

    message_one = NEW_BOT_UP_DATE_FOUND.format(
        branch_name=active_branch_name, changelog=changelog
    )
    message_two = NEW_UP_DATE_FOUND.format(branch_name=active_branch_name)

    if len(message_one) > 4095:
        with open("change.log", "w+", encoding="utf8") as out_file:
            out_file.write(str(message_one))
        await Don.send_message(
            message.chat_id, document="change.log", caption=message_two
        )
        os.remove("change.log")
    else:
        await message.edit(message_one)

    temp_upstream_remote.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit(
                        "Invalid APP Name. Please set the name of your bot in heroku in the var `HEROKU_APP_NAME.`"
                    )
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://", "https://api:" + HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(
                    deploy_start(Don, message, HEROKU_GIT_REF_SPEC, remote)
                )

            else:
                await message.edit(
                    "Please create the var `HEROKU_APP_NAME` as the key and the name of your bot in heroku as your value."
                )
                return
        else:
            await message.edit(NO_HEROKU_APP_CFGD)
    else:
        await message.edit("No heroku api key found in `HEROKU_API_KEY` var")


def generate_change_log(git_repo, diff_marker):
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in git_repo.iter_commits(diff_marker):
        out_put_str += f"â¢[{repo_change.committed_datetime.strftime(d_form)}]: {repo_change.summary} <{repo_change.author}>\n"
    return out_put_str


async def deploy_start(Don, message, refspec, remote):
    await message.edit(RESTARTING_APP)
    await message.edit(
        "Updated your TeamAlways SpamBot successfully sur!!!\nÂ© @Team_Always"
    )
    await remote.push(refspec=refspec)
    await Don.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)

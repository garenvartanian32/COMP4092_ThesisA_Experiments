def choose_jira_assignee(issue, asf_jira):
    """
    Prompt the user to choose who to assign the issue to in jira, given a list of candidates,
    including the original reporter and all commentors
    """
    while True:
        try:
            reporter = issue.fields.reporter
            commentors = map(lambda x: x.author, issue.fields.comment.comments)
            candidates = set(commentors)
            candidates.add(reporter)
            candidates = list(candidates)
            print("JIRA is unassigned, choose assignee")
            for idx, author in enumerate(candidates):
                if author.key == "apachespark":
                    continue
                annotations = ["Reporter"] if author == reporter else []
                if author in commentors:
                    annotations.append("Commentor")
                print("[%d] %s (%s)" % (idx, author.displayName, ",".join(annotations)))
            raw_assignee = input(
                "Enter number of user, or userid, to assign to (blank to leave unassigned):")
            if raw_assignee == "":
                return None
            else:
                try:
                    id = int(raw_assignee)
                    assignee = candidates[id]
                except:
                    # assume it's a user id, and try to assign (might fail, we just prompt again)
                    assignee = asf_jira.user(raw_assignee)
                asf_jira.assign_issue(issue.key, assignee.key)
                return assignee
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            print("Error assigning JIRA, try again (or leave blank and fix manually)")
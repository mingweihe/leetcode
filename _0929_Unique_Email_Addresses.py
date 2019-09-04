class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+', 1)[0].replace('.', '')
            # local_name = ''.join(local_name.split('+', 1)[0].split('.'))
            email_set.add(local_name + '@' + domain_name)
        return len(email_set)

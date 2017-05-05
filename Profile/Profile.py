# Profile classes
# Copyright LLIV

class session_Profile:
	def __init__(self, _xid, _start_date)
		self.xid = _xid
		self.start_date = _start_date

class session:
	def __init__(self, _start_date):
		self.start_Date = _start_date
		self.session_Profiles = []

	def addToSession(self, profile_xid, _start_date):
		# Add new profile to the session
		self.session_Profiles.Append(session_Profile(profile_xid, _start_date))

	def __interalRemoveFromSession(self, session_Profile):
		self.session_Profiles.remove(session_Profile)

	def __interalSortSessionProfiles(self):
		for i in range(0, len(self.session_Profiles) - 1):
			if self.session_Profiles[i].start_date < self.session_Profiles[i + 1].start_date:
				self.session_Profiles[i].start_date
	def __garbageCollection(self):


class profile_Manager:
	def __init__(self, _profile_Database):

		# Setup a new HashTable
		self.profiles = {}
		self.CurrentSession = 
		self.profile_Database = _profile_Database

	def getProfiles(self):
		# check if file is valid and read in the profiles to the hash
		# table.

	def __internalAddProfile(self,profile):
		# This function skips the check to see if the profile is 
		# already in the HashTable
		self.profiles[profile.profile_xid] = profile

	def __garbageCollection(self):


class profile_Circle:
	def __init__(self, _circle_name):
		self.circle_name = _circle_name
		self.profile_xids = []

	def addProfile(self, profile_xid):
		self.profile_xids.append(profile_xid)


class profile:
	def __init__(self, _profile_name, _start_date, _profile_xid):
		self.profile_name = _profile_name
		self.profile_xid = _profile_xid
		self.start_date = _start_date

		self.profile_circles = []
		self.profile_tags = []

	def generateJSON(self):
		# Generate JSON string of the profile

	def addCircle(self):
		# Add profile to a circle

	def addTag(self):
		# Add tag to profile

	def removeTag(self):
		# Remove tag from profile

	def removeCircle(self):
		# Remove profile from circle

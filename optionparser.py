# Copyright (c) 2013, RTP Network Services, Inc.
# All Rights Reserved      (904-236-6993)
# Vinod Halaharvi / vinod.halaharvi@rtpnet.net
# 
# http://www.rtpnet.net / codesupport@rtpnet.net
#
# There is NO warranty for this software.  If this software is used by
# someone else and passed on, the recipients should know that what they
# have is not the original, so that any problems introduced by others will
# not reflect on the original authors' reputations. This is *not* authorization
# to copy or distribute this software to others!

__all__ = ["OptionParser",]

class OptionParser(object):
	"""docstring for OptionParser"""
	def __init__(self, command, opts):
		super(OptionParser, self).__init__()
		self.opts =  opts
		self.command =  command

	def parse(self, line):
		"""docstring for parse"""
		words = [str(word).strip() for word in line.strip().split(",")]
		merge = zip(self.opts, words)
		posArgs =  words[len(merge):]
		return self.command + " " + " ".join([opt + " " +  word for opt, word in merge]) + " " + " ".join(posArgs)

CREATE TABLE `sites` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `URL` tinytext NOT NULL,
  `tagID` tinytext,
  `contentsHash` tinytext NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `slack` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `webhookURL` tinytext NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `slack-sites-link` (
  `siteID` int(11) NOT NULL,
  `slackID` int(11) NOT NULL,
  KEY `siteID` (`siteID`),
  KEY `slackID` (`slackID`),
  CONSTRAINT `slack-sites-link_ibfk_1` FOREIGN KEY (`siteID`) REFERENCES `sites` (`ID`) ON DELETE CASCADE,
  CONSTRAINT `slack-sites-link_ibfk_2` FOREIGN KEY (`slackID`) REFERENCES `slack` (`ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

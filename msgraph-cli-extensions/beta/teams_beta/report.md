# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az teams_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az teams_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az teams app-catalog|appCatalogs|[commands](#CommandsInappCatalogs)|
|az teams app-catalog-team-app|appCatalogs.teamsApps|[commands](#CommandsInappCatalogs.teamsApps)|
|az teams chat-chat|chats.chat|[commands](#CommandsInchats.chat)|
|az teams chat|chats|[commands](#CommandsInchats)|
|az teams chat-installed-app|chats.installedApps|[commands](#CommandsInchats.installedApps)|
|az teams chat-member|chats.members|[commands](#CommandsInchats.members)|
|az teams chat-message|chats.messages|[commands](#CommandsInchats.messages)|
|az teams chat-message-reply|chats.messages.replies|[commands](#CommandsInchats.messages.replies)|
|az teams chat-tab|chats.tabs|[commands](#CommandsInchats.tabs)|
|az teams group|groups|[commands](#CommandsIngroups)|
|az teams team|teams.team|[commands](#CommandsInteams.team)|
|az teams team|teams|[commands](#CommandsInteams)|
|az teams team-channel|teams.channels|[commands](#CommandsInteams.channels)|
|az teams team-channel-member|teams.channels.members|[commands](#CommandsInteams.channels.members)|
|az teams team-channel-message|teams.channels.messages|[commands](#CommandsInteams.channels.messages)|
|az teams team-channel-message-reply|teams.channels.messages.replies|[commands](#CommandsInteams.channels.messages.replies)|
|az teams team-channel-tab|teams.channels.tabs|[commands](#CommandsInteams.channels.tabs)|
|az teams team-installed-app|teams.installedApps|[commands](#CommandsInteams.installedApps)|
|az teams team-member|teams.members|[commands](#CommandsInteams.members)|
|az teams team-primary-channel|teams.primaryChannel|[commands](#CommandsInteams.primaryChannel)|
|az teams team-primary-channel-member|teams.primaryChannel.members|[commands](#CommandsInteams.primaryChannel.members)|
|az teams team-primary-channel-message|teams.primaryChannel.messages|[commands](#CommandsInteams.primaryChannel.messages)|
|az teams team-primary-channel-message-reply|teams.primaryChannel.messages.replies|[commands](#CommandsInteams.primaryChannel.messages.replies)|
|az teams team-primary-channel-tab|teams.primaryChannel.tabs|[commands](#CommandsInteams.primaryChannel.tabs)|
|az teams team-schedule|teams.schedule|[commands](#CommandsInteams.schedule)|
|az teams team-schedule-time-card|teams.schedule.timeCards|[commands](#CommandsInteams.schedule.timeCards)|
|az teams teamwork-teamwork|teamwork.teamwork|[commands](#CommandsInteamwork.teamwork)|
|az teams teamwork|teamwork|[commands](#CommandsInteamwork)|
|az teams user|users|[commands](#CommandsInusers)|
|az teams user-teamwork|users.teamwork|[commands](#CommandsInusers.teamwork)|
|az teams user-teamwork-installed-app|users.teamwork.installedApps|[commands](#CommandsInusers.teamwork.installedApps)|

## COMMANDS
### <a name="CommandsInappCatalogs">Commands in `az teams app-catalog` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams app-catalog create-team-app](#appCatalogsCreateTeamsApps)|CreateTeamsApps|[Parameters](#ParametersappCatalogsCreateTeamsApps)|Not Found|
|[az teams app-catalog delete-team-app](#appCatalogsDeleteTeamsApps)|DeleteTeamsApps|[Parameters](#ParametersappCatalogsDeleteTeamsApps)|Not Found|
|[az teams app-catalog list-team-app](#appCatalogsListTeamsApps)|ListTeamsApps|[Parameters](#ParametersappCatalogsListTeamsApps)|Not Found|
|[az teams app-catalog show-team-app](#appCatalogsGetTeamsApps)|GetTeamsApps|[Parameters](#ParametersappCatalogsGetTeamsApps)|Not Found|
|[az teams app-catalog update-team-app](#appCatalogsUpdateTeamsApps)|UpdateTeamsApps|[Parameters](#ParametersappCatalogsUpdateTeamsApps)|Not Found|

### <a name="CommandsInappCatalogs.teamsApps">Commands in `az teams app-catalog-team-app` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams app-catalog-team-app create-app-definition](#appCatalogs.teamsAppsCreateAppDefinitions)|CreateAppDefinitions|[Parameters](#ParametersappCatalogs.teamsAppsCreateAppDefinitions)|Not Found|
|[az teams app-catalog-team-app delete-app-definition](#appCatalogs.teamsAppsDeleteAppDefinitions)|DeleteAppDefinitions|[Parameters](#ParametersappCatalogs.teamsAppsDeleteAppDefinitions)|Not Found|
|[az teams app-catalog-team-app list-app-definition](#appCatalogs.teamsAppsListAppDefinitions)|ListAppDefinitions|[Parameters](#ParametersappCatalogs.teamsAppsListAppDefinitions)|Not Found|
|[az teams app-catalog-team-app show-app-definition](#appCatalogs.teamsAppsGetAppDefinitions)|GetAppDefinitions|[Parameters](#ParametersappCatalogs.teamsAppsGetAppDefinitions)|Not Found|
|[az teams app-catalog-team-app update-app-definition](#appCatalogs.teamsAppsUpdateAppDefinitions)|UpdateAppDefinitions|[Parameters](#ParametersappCatalogs.teamsAppsUpdateAppDefinitions)|Not Found|

### <a name="CommandsInchats">Commands in `az teams chat` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams chat all-message](#chatsallMessages)|allMessages|[Parameters](#ParameterschatsallMessages)|Not Found|
|[az teams chat create-installed-app](#chatsCreateInstalledApps)|CreateInstalledApps|[Parameters](#ParameterschatsCreateInstalledApps)|Not Found|
|[az teams chat create-member](#chatsCreateMembers)|CreateMembers|[Parameters](#ParameterschatsCreateMembers)|Not Found|
|[az teams chat create-message](#chatsCreateMessages)|CreateMessages|[Parameters](#ParameterschatsCreateMessages)|Not Found|
|[az teams chat create-tab](#chatsCreateTabs)|CreateTabs|[Parameters](#ParameterschatsCreateTabs)|Not Found|
|[az teams chat delete-installed-app](#chatsDeleteInstalledApps)|DeleteInstalledApps|[Parameters](#ParameterschatsDeleteInstalledApps)|Not Found|
|[az teams chat delete-member](#chatsDeleteMembers)|DeleteMembers|[Parameters](#ParameterschatsDeleteMembers)|Not Found|
|[az teams chat delete-message](#chatsDeleteMessages)|DeleteMessages|[Parameters](#ParameterschatsDeleteMessages)|Not Found|
|[az teams chat delete-tab](#chatsDeleteTabs)|DeleteTabs|[Parameters](#ParameterschatsDeleteTabs)|Not Found|
|[az teams chat list-installed-app](#chatsListInstalledApps)|ListInstalledApps|[Parameters](#ParameterschatsListInstalledApps)|Not Found|
|[az teams chat list-member](#chatsListMembers)|ListMembers|[Parameters](#ParameterschatsListMembers)|Not Found|
|[az teams chat list-message](#chatsListMessages)|ListMessages|[Parameters](#ParameterschatsListMessages)|Not Found|
|[az teams chat list-tab](#chatsListTabs)|ListTabs|[Parameters](#ParameterschatsListTabs)|Not Found|
|[az teams chat send-activity-notification](#chatssendActivityNotification)|sendActivityNotification|[Parameters](#ParameterschatssendActivityNotification)|Not Found|
|[az teams chat show-all-message](#chatsgetAllMessages)|getAllMessages|[Parameters](#ParameterschatsgetAllMessages)|Not Found|
|[az teams chat show-installed-app](#chatsGetInstalledApps)|GetInstalledApps|[Parameters](#ParameterschatsGetInstalledApps)|Not Found|
|[az teams chat show-member](#chatsGetMembers)|GetMembers|[Parameters](#ParameterschatsGetMembers)|Not Found|
|[az teams chat show-message](#chatsGetMessages)|GetMessages|[Parameters](#ParameterschatsGetMessages)|Not Found|
|[az teams chat show-tab](#chatsGetTabs)|GetTabs|[Parameters](#ParameterschatsGetTabs)|Not Found|
|[az teams chat update-installed-app](#chatsUpdateInstalledApps)|UpdateInstalledApps|[Parameters](#ParameterschatsUpdateInstalledApps)|Not Found|
|[az teams chat update-member](#chatsUpdateMembers)|UpdateMembers|[Parameters](#ParameterschatsUpdateMembers)|Not Found|
|[az teams chat update-message](#chatsUpdateMessages)|UpdateMessages|[Parameters](#ParameterschatsUpdateMessages)|Not Found|
|[az teams chat update-tab](#chatsUpdateTabs)|UpdateTabs|[Parameters](#ParameterschatsUpdateTabs)|Not Found|

### <a name="CommandsInchats.chat">Commands in `az teams chat-chat` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams chat-chat create-chat](#chats.chatCreateChat)|CreateChat|[Parameters](#Parameterschats.chatCreateChat)|Not Found|
|[az teams chat-chat delete-chat](#chats.chatDeleteChat)|DeleteChat|[Parameters](#Parameterschats.chatDeleteChat)|Not Found|
|[az teams chat-chat list-chat](#chats.chatListChat)|ListChat|[Parameters](#Parameterschats.chatListChat)|Not Found|
|[az teams chat-chat show-chat](#chats.chatGetChat)|GetChat|[Parameters](#Parameterschats.chatGetChat)|Not Found|
|[az teams chat-chat update-chat](#chats.chatUpdateChat)|UpdateChat|[Parameters](#Parameterschats.chatUpdateChat)|Not Found|

### <a name="CommandsInchats.installedApps">Commands in `az teams chat-installed-app` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams chat-installed-app delete-ref-team-app](#chats.installedAppsDeleteRefTeamsApp)|DeleteRefTeamsApp|[Parameters](#Parameterschats.installedAppsDeleteRefTeamsApp)|Not Found|
|[az teams chat-installed-app delete-ref-team-app-definition](#chats.installedAppsDeleteRefTeamsAppDefinition)|DeleteRefTeamsAppDefinition|[Parameters](#Parameterschats.installedAppsDeleteRefTeamsAppDefinition)|Not Found|
|[az teams chat-installed-app set-ref-team-app](#chats.installedAppsSetRefTeamsApp)|SetRefTeamsApp|[Parameters](#Parameterschats.installedAppsSetRefTeamsApp)|Not Found|
|[az teams chat-installed-app set-ref-team-app-definition](#chats.installedAppsSetRefTeamsAppDefinition)|SetRefTeamsAppDefinition|[Parameters](#Parameterschats.installedAppsSetRefTeamsAppDefinition)|Not Found|
|[az teams chat-installed-app show-ref-team-app](#chats.installedAppsGetRefTeamsApp)|GetRefTeamsApp|[Parameters](#Parameterschats.installedAppsGetRefTeamsApp)|Not Found|
|[az teams chat-installed-app show-ref-team-app-definition](#chats.installedAppsGetRefTeamsAppDefinition)|GetRefTeamsAppDefinition|[Parameters](#Parameterschats.installedAppsGetRefTeamsAppDefinition)|Not Found|
|[az teams chat-installed-app show-team-app](#chats.installedAppsGetTeamsApp)|GetTeamsApp|[Parameters](#Parameterschats.installedAppsGetTeamsApp)|Not Found|
|[az teams chat-installed-app show-team-app-definition](#chats.installedAppsGetTeamsAppDefinition)|GetTeamsAppDefinition|[Parameters](#Parameterschats.installedAppsGetTeamsAppDefinition)|Not Found|
|[az teams chat-installed-app upgrade](#chats.installedAppsupgrade)|upgrade|[Parameters](#Parameterschats.installedAppsupgrade)|Not Found|

### <a name="CommandsInchats.members">Commands in `az teams chat-member` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams chat-member add](#chats.membersadd)|add|[Parameters](#Parameterschats.membersadd)|Not Found|

### <a name="CommandsInchats.messages">Commands in `az teams chat-message` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams chat-message create-hosted-content](#chats.messagesCreateHostedContents)|CreateHostedContents|[Parameters](#Parameterschats.messagesCreateHostedContents)|Not Found|
|[az teams chat-message create-reply](#chats.messagesCreateReplies)|CreateReplies|[Parameters](#Parameterschats.messagesCreateReplies)|Not Found|
|[az teams chat-message delete-hosted-content](#chats.messagesDeleteHostedContents)|DeleteHostedContents|[Parameters](#Parameterschats.messagesDeleteHostedContents)|Not Found|
|[az teams chat-message delete-reply](#chats.messagesDeleteReplies)|DeleteReplies|[Parameters](#Parameterschats.messagesDeleteReplies)|Not Found|
|[az teams chat-message delta](#chats.messagesdelta)|delta|[Parameters](#Parameterschats.messagesdelta)|Not Found|
|[az teams chat-message list-hosted-content](#chats.messagesListHostedContents)|ListHostedContents|[Parameters](#Parameterschats.messagesListHostedContents)|Not Found|
|[az teams chat-message list-reply](#chats.messagesListReplies)|ListReplies|[Parameters](#Parameterschats.messagesListReplies)|Not Found|
|[az teams chat-message set-hosted-content-content](#chats.messagesSetHostedContentsContent)|SetHostedContentsContent|[Parameters](#Parameterschats.messagesSetHostedContentsContent)|Not Found|
|[az teams chat-message show-hosted-content](#chats.messagesGetHostedContents)|GetHostedContents|[Parameters](#Parameterschats.messagesGetHostedContents)|Not Found|
|[az teams chat-message show-hosted-content-content](#chats.messagesGetHostedContentsContent)|GetHostedContentsContent|[Parameters](#Parameterschats.messagesGetHostedContentsContent)|Not Found|
|[az teams chat-message show-reply](#chats.messagesGetReplies)|GetReplies|[Parameters](#Parameterschats.messagesGetReplies)|Not Found|
|[az teams chat-message update-hosted-content](#chats.messagesUpdateHostedContents)|UpdateHostedContents|[Parameters](#Parameterschats.messagesUpdateHostedContents)|Not Found|
|[az teams chat-message update-reply](#chats.messagesUpdateReplies)|UpdateReplies|[Parameters](#Parameterschats.messagesUpdateReplies)|Not Found|

### <a name="CommandsInchats.messages.replies">Commands in `az teams chat-message-reply` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams chat-message-reply delta](#chats.messages.repliesdelta)|delta|[Parameters](#Parameterschats.messages.repliesdelta)|Not Found|

### <a name="CommandsInchats.tabs">Commands in `az teams chat-tab` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams chat-tab delete-ref-team-app](#chats.tabsDeleteRefTeamsApp)|DeleteRefTeamsApp|[Parameters](#Parameterschats.tabsDeleteRefTeamsApp)|Not Found|
|[az teams chat-tab set-ref-team-app](#chats.tabsSetRefTeamsApp)|SetRefTeamsApp|[Parameters](#Parameterschats.tabsSetRefTeamsApp)|Not Found|
|[az teams chat-tab show-ref-team-app](#chats.tabsGetRefTeamsApp)|GetRefTeamsApp|[Parameters](#Parameterschats.tabsGetRefTeamsApp)|Not Found|
|[az teams chat-tab show-team-app](#chats.tabsGetTeamsApp)|GetTeamsApp|[Parameters](#Parameterschats.tabsGetTeamsApp)|Not Found|

### <a name="CommandsIngroups">Commands in `az teams group` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams group delete-team](#groupsDeleteTeam)|DeleteTeam|[Parameters](#ParametersgroupsDeleteTeam)|Not Found|
|[az teams group show-team](#groupsGetTeam)|GetTeam|[Parameters](#ParametersgroupsGetTeam)|Not Found|
|[az teams group update-team](#groupsUpdateTeam)|UpdateTeam|[Parameters](#ParametersgroupsUpdateTeam)|Not Found|

### <a name="CommandsInteams.team">Commands in `az teams team` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team list](#teams.teamListTeam)|ListTeam|[Parameters](#Parametersteams.teamListTeam)|Not Found|
|[az teams team create](#teams.teamCreateTeam)|CreateTeam|[Parameters](#Parametersteams.teamCreateTeam)|Not Found|
|[az teams team update](#teams.teamUpdateTeam)|UpdateTeam|[Parameters](#Parametersteams.teamUpdateTeam)|Not Found|
|[az teams team delete-team](#teams.teamDeleteTeam)|DeleteTeam|[Parameters](#Parametersteams.teamDeleteTeam)|Not Found|
|[az teams team show-team](#teams.teamGetTeam)|GetTeam|[Parameters](#Parametersteams.teamGetTeam)|Not Found|

### <a name="CommandsInteams">Commands in `az teams team` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team all-message](#teamsallMessages)|allMessages|[Parameters](#ParametersteamsallMessages)|Not Found|
|[az teams team archive](#teamsarchive)|archive|[Parameters](#Parametersteamsarchive)|Not Found|
|[az teams team clone](#teamsclone)|clone|[Parameters](#Parametersteamsclone)|Not Found|
|[az teams team complete-migration](#teamscompleteMigration)|completeMigration|[Parameters](#ParametersteamscompleteMigration)|Not Found|
|[az teams team create-channel](#teamsCreateChannels)|CreateChannels|[Parameters](#ParametersteamsCreateChannels)|Not Found|
|[az teams team create-installed-app](#teamsCreateInstalledApps)|CreateInstalledApps|[Parameters](#ParametersteamsCreateInstalledApps)|Not Found|
|[az teams team create-member](#teamsCreateMembers)|CreateMembers|[Parameters](#ParametersteamsCreateMembers)|Not Found|
|[az teams team create-operation](#teamsCreateOperations)|CreateOperations|[Parameters](#ParametersteamsCreateOperations)|Not Found|
|[az teams team create-ref-owner](#teamsCreateRefOwners)|CreateRefOwners|[Parameters](#ParametersteamsCreateRefOwners)|Not Found|
|[az teams team delete-channel](#teamsDeleteChannels)|DeleteChannels|[Parameters](#ParametersteamsDeleteChannels)|Not Found|
|[az teams team delete-installed-app](#teamsDeleteInstalledApps)|DeleteInstalledApps|[Parameters](#ParametersteamsDeleteInstalledApps)|Not Found|
|[az teams team delete-member](#teamsDeleteMembers)|DeleteMembers|[Parameters](#ParametersteamsDeleteMembers)|Not Found|
|[az teams team delete-operation](#teamsDeleteOperations)|DeleteOperations|[Parameters](#ParametersteamsDeleteOperations)|Not Found|
|[az teams team delete-photo](#teamsDeletePhoto)|DeletePhoto|[Parameters](#ParametersteamsDeletePhoto)|Not Found|
|[az teams team delete-primary-channel](#teamsDeletePrimaryChannel)|DeletePrimaryChannel|[Parameters](#ParametersteamsDeletePrimaryChannel)|Not Found|
|[az teams team delete-ref-group](#teamsDeleteRefGroup)|DeleteRefGroup|[Parameters](#ParametersteamsDeleteRefGroup)|Not Found|
|[az teams team delete-ref-template](#teamsDeleteRefTemplate)|DeleteRefTemplate|[Parameters](#ParametersteamsDeleteRefTemplate)|Not Found|
|[az teams team delete-schedule](#teamsDeleteSchedule)|DeleteSchedule|[Parameters](#ParametersteamsDeleteSchedule)|Not Found|
|[az teams team list-channel](#teamsListChannels)|ListChannels|[Parameters](#ParametersteamsListChannels)|Not Found|
|[az teams team list-installed-app](#teamsListInstalledApps)|ListInstalledApps|[Parameters](#ParametersteamsListInstalledApps)|Not Found|
|[az teams team list-member](#teamsListMembers)|ListMembers|[Parameters](#ParametersteamsListMembers)|Not Found|
|[az teams team list-operation](#teamsListOperations)|ListOperations|[Parameters](#ParametersteamsListOperations)|Not Found|
|[az teams team list-owner](#teamsListOwners)|ListOwners|[Parameters](#ParametersteamsListOwners)|Not Found|
|[az teams team list-ref-owner](#teamsListRefOwners)|ListRefOwners|[Parameters](#ParametersteamsListRefOwners)|Not Found|
|[az teams team send-activity-notification](#teamssendActivityNotification)|sendActivityNotification|[Parameters](#ParametersteamssendActivityNotification)|Not Found|
|[az teams team set-photo-content](#teamsSetPhotoContent)|SetPhotoContent|[Parameters](#ParametersteamsSetPhotoContent)|Not Found|
|[az teams team set-ref-group](#teamsSetRefGroup)|SetRefGroup|[Parameters](#ParametersteamsSetRefGroup)|Not Found|
|[az teams team set-ref-template](#teamsSetRefTemplate)|SetRefTemplate|[Parameters](#ParametersteamsSetRefTemplate)|Not Found|
|[az teams team show-all-message](#teamsgetAllMessages)|getAllMessages|[Parameters](#ParametersteamsgetAllMessages)|Not Found|
|[az teams team show-channel](#teamsGetChannels)|GetChannels|[Parameters](#ParametersteamsGetChannels)|Not Found|
|[az teams team show-group](#teamsGetGroup)|GetGroup|[Parameters](#ParametersteamsGetGroup)|Not Found|
|[az teams team show-installed-app](#teamsGetInstalledApps)|GetInstalledApps|[Parameters](#ParametersteamsGetInstalledApps)|Not Found|
|[az teams team show-member](#teamsGetMembers)|GetMembers|[Parameters](#ParametersteamsGetMembers)|Not Found|
|[az teams team show-operation](#teamsGetOperations)|GetOperations|[Parameters](#ParametersteamsGetOperations)|Not Found|
|[az teams team show-photo](#teamsGetPhoto)|GetPhoto|[Parameters](#ParametersteamsGetPhoto)|Not Found|
|[az teams team show-photo-content](#teamsGetPhotoContent)|GetPhotoContent|[Parameters](#ParametersteamsGetPhotoContent)|Not Found|
|[az teams team show-primary-channel](#teamsGetPrimaryChannel)|GetPrimaryChannel|[Parameters](#ParametersteamsGetPrimaryChannel)|Not Found|
|[az teams team show-ref-group](#teamsGetRefGroup)|GetRefGroup|[Parameters](#ParametersteamsGetRefGroup)|Not Found|
|[az teams team show-ref-template](#teamsGetRefTemplate)|GetRefTemplate|[Parameters](#ParametersteamsGetRefTemplate)|Not Found|
|[az teams team show-schedule](#teamsGetSchedule)|GetSchedule|[Parameters](#ParametersteamsGetSchedule)|Not Found|
|[az teams team show-template](#teamsGetTemplate)|GetTemplate|[Parameters](#ParametersteamsGetTemplate)|Not Found|
|[az teams team unarchive](#teamsunarchive)|unarchive|[Parameters](#Parametersteamsunarchive)|Not Found|
|[az teams team update-channel](#teamsUpdateChannels)|UpdateChannels|[Parameters](#ParametersteamsUpdateChannels)|Not Found|
|[az teams team update-installed-app](#teamsUpdateInstalledApps)|UpdateInstalledApps|[Parameters](#ParametersteamsUpdateInstalledApps)|Not Found|
|[az teams team update-member](#teamsUpdateMembers)|UpdateMembers|[Parameters](#ParametersteamsUpdateMembers)|Not Found|
|[az teams team update-operation](#teamsUpdateOperations)|UpdateOperations|[Parameters](#ParametersteamsUpdateOperations)|Not Found|
|[az teams team update-photo](#teamsUpdatePhoto)|UpdatePhoto|[Parameters](#ParametersteamsUpdatePhoto)|Not Found|
|[az teams team update-primary-channel](#teamsUpdatePrimaryChannel)|UpdatePrimaryChannel|[Parameters](#ParametersteamsUpdatePrimaryChannel)|Not Found|
|[az teams team update-schedule](#teamsUpdateSchedule)|UpdateSchedule|[Parameters](#ParametersteamsUpdateSchedule)|Not Found|

### <a name="CommandsInteams.channels">Commands in `az teams team-channel` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-channel all-message](#teams.channelsallMessages)|allMessages|[Parameters](#Parametersteams.channelsallMessages)|Not Found|
|[az teams team-channel complete-migration](#teams.channelscompleteMigration)|completeMigration|[Parameters](#Parametersteams.channelscompleteMigration)|Not Found|
|[az teams team-channel create-member](#teams.channelsCreateMembers)|CreateMembers|[Parameters](#Parametersteams.channelsCreateMembers)|Not Found|
|[az teams team-channel create-message](#teams.channelsCreateMessages)|CreateMessages|[Parameters](#Parametersteams.channelsCreateMessages)|Not Found|
|[az teams team-channel create-tab](#teams.channelsCreateTabs)|CreateTabs|[Parameters](#Parametersteams.channelsCreateTabs)|Not Found|
|[az teams team-channel delete-file-folder](#teams.channelsDeleteFilesFolder)|DeleteFilesFolder|[Parameters](#Parametersteams.channelsDeleteFilesFolder)|Not Found|
|[az teams team-channel delete-member](#teams.channelsDeleteMembers)|DeleteMembers|[Parameters](#Parametersteams.channelsDeleteMembers)|Not Found|
|[az teams team-channel delete-message](#teams.channelsDeleteMessages)|DeleteMessages|[Parameters](#Parametersteams.channelsDeleteMessages)|Not Found|
|[az teams team-channel delete-tab](#teams.channelsDeleteTabs)|DeleteTabs|[Parameters](#Parametersteams.channelsDeleteTabs)|Not Found|
|[az teams team-channel list-member](#teams.channelsListMembers)|ListMembers|[Parameters](#Parametersteams.channelsListMembers)|Not Found|
|[az teams team-channel list-message](#teams.channelsListMessages)|ListMessages|[Parameters](#Parametersteams.channelsListMessages)|Not Found|
|[az teams team-channel list-tab](#teams.channelsListTabs)|ListTabs|[Parameters](#Parametersteams.channelsListTabs)|Not Found|
|[az teams team-channel set-file-folder-content](#teams.channelsSetFilesFolderContent)|SetFilesFolderContent|[Parameters](#Parametersteams.channelsSetFilesFolderContent)|Not Found|
|[az teams team-channel show-file-folder](#teams.channelsGetFilesFolder)|GetFilesFolder|[Parameters](#Parametersteams.channelsGetFilesFolder)|Not Found|
|[az teams team-channel show-file-folder-content](#teams.channelsGetFilesFolderContent)|GetFilesFolderContent|[Parameters](#Parametersteams.channelsGetFilesFolderContent)|Not Found|
|[az teams team-channel show-member](#teams.channelsGetMembers)|GetMembers|[Parameters](#Parametersteams.channelsGetMembers)|Not Found|
|[az teams team-channel show-message](#teams.channelsGetMessages)|GetMessages|[Parameters](#Parametersteams.channelsGetMessages)|Not Found|
|[az teams team-channel show-tab](#teams.channelsGetTabs)|GetTabs|[Parameters](#Parametersteams.channelsGetTabs)|Not Found|
|[az teams team-channel update-file-folder](#teams.channelsUpdateFilesFolder)|UpdateFilesFolder|[Parameters](#Parametersteams.channelsUpdateFilesFolder)|Not Found|
|[az teams team-channel update-member](#teams.channelsUpdateMembers)|UpdateMembers|[Parameters](#Parametersteams.channelsUpdateMembers)|Not Found|
|[az teams team-channel update-message](#teams.channelsUpdateMessages)|UpdateMessages|[Parameters](#Parametersteams.channelsUpdateMessages)|Not Found|
|[az teams team-channel update-tab](#teams.channelsUpdateTabs)|UpdateTabs|[Parameters](#Parametersteams.channelsUpdateTabs)|Not Found|

### <a name="CommandsInteams.channels.members">Commands in `az teams team-channel-member` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-channel-member add](#teams.channels.membersadd)|add|[Parameters](#Parametersteams.channels.membersadd)|Not Found|

### <a name="CommandsInteams.channels.messages">Commands in `az teams team-channel-message` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-channel-message create-hosted-content](#teams.channels.messagesCreateHostedContents)|CreateHostedContents|[Parameters](#Parametersteams.channels.messagesCreateHostedContents)|Not Found|
|[az teams team-channel-message create-reply](#teams.channels.messagesCreateReplies)|CreateReplies|[Parameters](#Parametersteams.channels.messagesCreateReplies)|Not Found|
|[az teams team-channel-message delete-hosted-content](#teams.channels.messagesDeleteHostedContents)|DeleteHostedContents|[Parameters](#Parametersteams.channels.messagesDeleteHostedContents)|Not Found|
|[az teams team-channel-message delete-reply](#teams.channels.messagesDeleteReplies)|DeleteReplies|[Parameters](#Parametersteams.channels.messagesDeleteReplies)|Not Found|
|[az teams team-channel-message delta](#teams.channels.messagesdelta)|delta|[Parameters](#Parametersteams.channels.messagesdelta)|Not Found|
|[az teams team-channel-message list-hosted-content](#teams.channels.messagesListHostedContents)|ListHostedContents|[Parameters](#Parametersteams.channels.messagesListHostedContents)|Not Found|
|[az teams team-channel-message list-reply](#teams.channels.messagesListReplies)|ListReplies|[Parameters](#Parametersteams.channels.messagesListReplies)|Not Found|
|[az teams team-channel-message set-hosted-content-content](#teams.channels.messagesSetHostedContentsContent)|SetHostedContentsContent|[Parameters](#Parametersteams.channels.messagesSetHostedContentsContent)|Not Found|
|[az teams team-channel-message show-hosted-content](#teams.channels.messagesGetHostedContents)|GetHostedContents|[Parameters](#Parametersteams.channels.messagesGetHostedContents)|Not Found|
|[az teams team-channel-message show-hosted-content-content](#teams.channels.messagesGetHostedContentsContent)|GetHostedContentsContent|[Parameters](#Parametersteams.channels.messagesGetHostedContentsContent)|Not Found|
|[az teams team-channel-message show-reply](#teams.channels.messagesGetReplies)|GetReplies|[Parameters](#Parametersteams.channels.messagesGetReplies)|Not Found|
|[az teams team-channel-message update-hosted-content](#teams.channels.messagesUpdateHostedContents)|UpdateHostedContents|[Parameters](#Parametersteams.channels.messagesUpdateHostedContents)|Not Found|
|[az teams team-channel-message update-reply](#teams.channels.messagesUpdateReplies)|UpdateReplies|[Parameters](#Parametersteams.channels.messagesUpdateReplies)|Not Found|

### <a name="CommandsInteams.channels.messages.replies">Commands in `az teams team-channel-message-reply` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-channel-message-reply delta](#teams.channels.messages.repliesdelta)|delta|[Parameters](#Parametersteams.channels.messages.repliesdelta)|Not Found|

### <a name="CommandsInteams.channels.tabs">Commands in `az teams team-channel-tab` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-channel-tab delete-ref-team-app](#teams.channels.tabsDeleteRefTeamsApp)|DeleteRefTeamsApp|[Parameters](#Parametersteams.channels.tabsDeleteRefTeamsApp)|Not Found|
|[az teams team-channel-tab set-ref-team-app](#teams.channels.tabsSetRefTeamsApp)|SetRefTeamsApp|[Parameters](#Parametersteams.channels.tabsSetRefTeamsApp)|Not Found|
|[az teams team-channel-tab show-ref-team-app](#teams.channels.tabsGetRefTeamsApp)|GetRefTeamsApp|[Parameters](#Parametersteams.channels.tabsGetRefTeamsApp)|Not Found|
|[az teams team-channel-tab show-team-app](#teams.channels.tabsGetTeamsApp)|GetTeamsApp|[Parameters](#Parametersteams.channels.tabsGetTeamsApp)|Not Found|

### <a name="CommandsInteams.installedApps">Commands in `az teams team-installed-app` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-installed-app delete-ref-team-app](#teams.installedAppsDeleteRefTeamsApp)|DeleteRefTeamsApp|[Parameters](#Parametersteams.installedAppsDeleteRefTeamsApp)|Not Found|
|[az teams team-installed-app delete-ref-team-app-definition](#teams.installedAppsDeleteRefTeamsAppDefinition)|DeleteRefTeamsAppDefinition|[Parameters](#Parametersteams.installedAppsDeleteRefTeamsAppDefinition)|Not Found|
|[az teams team-installed-app set-ref-team-app](#teams.installedAppsSetRefTeamsApp)|SetRefTeamsApp|[Parameters](#Parametersteams.installedAppsSetRefTeamsApp)|Not Found|
|[az teams team-installed-app set-ref-team-app-definition](#teams.installedAppsSetRefTeamsAppDefinition)|SetRefTeamsAppDefinition|[Parameters](#Parametersteams.installedAppsSetRefTeamsAppDefinition)|Not Found|
|[az teams team-installed-app show-ref-team-app](#teams.installedAppsGetRefTeamsApp)|GetRefTeamsApp|[Parameters](#Parametersteams.installedAppsGetRefTeamsApp)|Not Found|
|[az teams team-installed-app show-ref-team-app-definition](#teams.installedAppsGetRefTeamsAppDefinition)|GetRefTeamsAppDefinition|[Parameters](#Parametersteams.installedAppsGetRefTeamsAppDefinition)|Not Found|
|[az teams team-installed-app show-team-app](#teams.installedAppsGetTeamsApp)|GetTeamsApp|[Parameters](#Parametersteams.installedAppsGetTeamsApp)|Not Found|
|[az teams team-installed-app show-team-app-definition](#teams.installedAppsGetTeamsAppDefinition)|GetTeamsAppDefinition|[Parameters](#Parametersteams.installedAppsGetTeamsAppDefinition)|Not Found|
|[az teams team-installed-app upgrade](#teams.installedAppsupgrade)|upgrade|[Parameters](#Parametersteams.installedAppsupgrade)|Not Found|

### <a name="CommandsInteams.members">Commands in `az teams team-member` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-member add](#teams.membersadd)|add|[Parameters](#Parametersteams.membersadd)|Not Found|

### <a name="CommandsInteams.primaryChannel">Commands in `az teams team-primary-channel` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-primary-channel complete-migration](#teams.primaryChannelcompleteMigration)|completeMigration|[Parameters](#Parametersteams.primaryChannelcompleteMigration)|Not Found|
|[az teams team-primary-channel create-member](#teams.primaryChannelCreateMembers)|CreateMembers|[Parameters](#Parametersteams.primaryChannelCreateMembers)|Not Found|
|[az teams team-primary-channel create-message](#teams.primaryChannelCreateMessages)|CreateMessages|[Parameters](#Parametersteams.primaryChannelCreateMessages)|Not Found|
|[az teams team-primary-channel create-tab](#teams.primaryChannelCreateTabs)|CreateTabs|[Parameters](#Parametersteams.primaryChannelCreateTabs)|Not Found|
|[az teams team-primary-channel delete-file-folder](#teams.primaryChannelDeleteFilesFolder)|DeleteFilesFolder|[Parameters](#Parametersteams.primaryChannelDeleteFilesFolder)|Not Found|
|[az teams team-primary-channel delete-member](#teams.primaryChannelDeleteMembers)|DeleteMembers|[Parameters](#Parametersteams.primaryChannelDeleteMembers)|Not Found|
|[az teams team-primary-channel delete-message](#teams.primaryChannelDeleteMessages)|DeleteMessages|[Parameters](#Parametersteams.primaryChannelDeleteMessages)|Not Found|
|[az teams team-primary-channel delete-tab](#teams.primaryChannelDeleteTabs)|DeleteTabs|[Parameters](#Parametersteams.primaryChannelDeleteTabs)|Not Found|
|[az teams team-primary-channel list-member](#teams.primaryChannelListMembers)|ListMembers|[Parameters](#Parametersteams.primaryChannelListMembers)|Not Found|
|[az teams team-primary-channel list-message](#teams.primaryChannelListMessages)|ListMessages|[Parameters](#Parametersteams.primaryChannelListMessages)|Not Found|
|[az teams team-primary-channel list-tab](#teams.primaryChannelListTabs)|ListTabs|[Parameters](#Parametersteams.primaryChannelListTabs)|Not Found|
|[az teams team-primary-channel set-file-folder-content](#teams.primaryChannelSetFilesFolderContent)|SetFilesFolderContent|[Parameters](#Parametersteams.primaryChannelSetFilesFolderContent)|Not Found|
|[az teams team-primary-channel show-file-folder](#teams.primaryChannelGetFilesFolder)|GetFilesFolder|[Parameters](#Parametersteams.primaryChannelGetFilesFolder)|Not Found|
|[az teams team-primary-channel show-file-folder-content](#teams.primaryChannelGetFilesFolderContent)|GetFilesFolderContent|[Parameters](#Parametersteams.primaryChannelGetFilesFolderContent)|Not Found|
|[az teams team-primary-channel show-member](#teams.primaryChannelGetMembers)|GetMembers|[Parameters](#Parametersteams.primaryChannelGetMembers)|Not Found|
|[az teams team-primary-channel show-message](#teams.primaryChannelGetMessages)|GetMessages|[Parameters](#Parametersteams.primaryChannelGetMessages)|Not Found|
|[az teams team-primary-channel show-tab](#teams.primaryChannelGetTabs)|GetTabs|[Parameters](#Parametersteams.primaryChannelGetTabs)|Not Found|
|[az teams team-primary-channel update-file-folder](#teams.primaryChannelUpdateFilesFolder)|UpdateFilesFolder|[Parameters](#Parametersteams.primaryChannelUpdateFilesFolder)|Not Found|
|[az teams team-primary-channel update-member](#teams.primaryChannelUpdateMembers)|UpdateMembers|[Parameters](#Parametersteams.primaryChannelUpdateMembers)|Not Found|
|[az teams team-primary-channel update-message](#teams.primaryChannelUpdateMessages)|UpdateMessages|[Parameters](#Parametersteams.primaryChannelUpdateMessages)|Not Found|
|[az teams team-primary-channel update-tab](#teams.primaryChannelUpdateTabs)|UpdateTabs|[Parameters](#Parametersteams.primaryChannelUpdateTabs)|Not Found|

### <a name="CommandsInteams.primaryChannel.members">Commands in `az teams team-primary-channel-member` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-primary-channel-member add](#teams.primaryChannel.membersadd)|add|[Parameters](#Parametersteams.primaryChannel.membersadd)|Not Found|

### <a name="CommandsInteams.primaryChannel.messages">Commands in `az teams team-primary-channel-message` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-primary-channel-message create-hosted-content](#teams.primaryChannel.messagesCreateHostedContents)|CreateHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesCreateHostedContents)|Not Found|
|[az teams team-primary-channel-message create-reply](#teams.primaryChannel.messagesCreateReplies)|CreateReplies|[Parameters](#Parametersteams.primaryChannel.messagesCreateReplies)|Not Found|
|[az teams team-primary-channel-message delete-hosted-content](#teams.primaryChannel.messagesDeleteHostedContents)|DeleteHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesDeleteHostedContents)|Not Found|
|[az teams team-primary-channel-message delete-reply](#teams.primaryChannel.messagesDeleteReplies)|DeleteReplies|[Parameters](#Parametersteams.primaryChannel.messagesDeleteReplies)|Not Found|
|[az teams team-primary-channel-message delta](#teams.primaryChannel.messagesdelta)|delta|[Parameters](#Parametersteams.primaryChannel.messagesdelta)|Not Found|
|[az teams team-primary-channel-message list-hosted-content](#teams.primaryChannel.messagesListHostedContents)|ListHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesListHostedContents)|Not Found|
|[az teams team-primary-channel-message list-reply](#teams.primaryChannel.messagesListReplies)|ListReplies|[Parameters](#Parametersteams.primaryChannel.messagesListReplies)|Not Found|
|[az teams team-primary-channel-message set-hosted-content-content](#teams.primaryChannel.messagesSetHostedContentsContent)|SetHostedContentsContent|[Parameters](#Parametersteams.primaryChannel.messagesSetHostedContentsContent)|Not Found|
|[az teams team-primary-channel-message show-hosted-content](#teams.primaryChannel.messagesGetHostedContents)|GetHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesGetHostedContents)|Not Found|
|[az teams team-primary-channel-message show-hosted-content-content](#teams.primaryChannel.messagesGetHostedContentsContent)|GetHostedContentsContent|[Parameters](#Parametersteams.primaryChannel.messagesGetHostedContentsContent)|Not Found|
|[az teams team-primary-channel-message show-reply](#teams.primaryChannel.messagesGetReplies)|GetReplies|[Parameters](#Parametersteams.primaryChannel.messagesGetReplies)|Not Found|
|[az teams team-primary-channel-message update-hosted-content](#teams.primaryChannel.messagesUpdateHostedContents)|UpdateHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesUpdateHostedContents)|Not Found|
|[az teams team-primary-channel-message update-reply](#teams.primaryChannel.messagesUpdateReplies)|UpdateReplies|[Parameters](#Parametersteams.primaryChannel.messagesUpdateReplies)|Not Found|

### <a name="CommandsInteams.primaryChannel.messages.replies">Commands in `az teams team-primary-channel-message-reply` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-primary-channel-message-reply delta](#teams.primaryChannel.messages.repliesdelta)|delta|[Parameters](#Parametersteams.primaryChannel.messages.repliesdelta)|Not Found|

### <a name="CommandsInteams.primaryChannel.tabs">Commands in `az teams team-primary-channel-tab` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-primary-channel-tab delete-ref-team-app](#teams.primaryChannel.tabsDeleteRefTeamsApp)|DeleteRefTeamsApp|[Parameters](#Parametersteams.primaryChannel.tabsDeleteRefTeamsApp)|Not Found|
|[az teams team-primary-channel-tab set-ref-team-app](#teams.primaryChannel.tabsSetRefTeamsApp)|SetRefTeamsApp|[Parameters](#Parametersteams.primaryChannel.tabsSetRefTeamsApp)|Not Found|
|[az teams team-primary-channel-tab show-ref-team-app](#teams.primaryChannel.tabsGetRefTeamsApp)|GetRefTeamsApp|[Parameters](#Parametersteams.primaryChannel.tabsGetRefTeamsApp)|Not Found|
|[az teams team-primary-channel-tab show-team-app](#teams.primaryChannel.tabsGetTeamsApp)|GetTeamsApp|[Parameters](#Parametersteams.primaryChannel.tabsGetTeamsApp)|Not Found|

### <a name="CommandsInteams.schedule">Commands in `az teams team-schedule` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-schedule create-offer-shift-request](#teams.scheduleCreateOfferShiftRequests)|CreateOfferShiftRequests|[Parameters](#Parametersteams.scheduleCreateOfferShiftRequests)|Not Found|
|[az teams team-schedule create-open-shift](#teams.scheduleCreateOpenShifts)|CreateOpenShifts|[Parameters](#Parametersteams.scheduleCreateOpenShifts)|Not Found|
|[az teams team-schedule create-open-shift-change-request](#teams.scheduleCreateOpenShiftChangeRequests)|CreateOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleCreateOpenShiftChangeRequests)|Not Found|
|[az teams team-schedule create-scheduling-group](#teams.scheduleCreateSchedulingGroups)|CreateSchedulingGroups|[Parameters](#Parametersteams.scheduleCreateSchedulingGroups)|Not Found|
|[az teams team-schedule create-shift](#teams.scheduleCreateShifts)|CreateShifts|[Parameters](#Parametersteams.scheduleCreateShifts)|Not Found|
|[az teams team-schedule create-swap-shift-change-request](#teams.scheduleCreateSwapShiftsChangeRequests)|CreateSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleCreateSwapShiftsChangeRequests)|Not Found|
|[az teams team-schedule create-time-card](#teams.scheduleCreateTimeCards)|CreateTimeCards|[Parameters](#Parametersteams.scheduleCreateTimeCards)|Not Found|
|[az teams team-schedule create-time-off](#teams.scheduleCreateTimesOff)|CreateTimesOff|[Parameters](#Parametersteams.scheduleCreateTimesOff)|Not Found|
|[az teams team-schedule create-time-off-reason](#teams.scheduleCreateTimeOffReasons)|CreateTimeOffReasons|[Parameters](#Parametersteams.scheduleCreateTimeOffReasons)|Not Found|
|[az teams team-schedule create-time-off-request](#teams.scheduleCreateTimeOffRequests)|CreateTimeOffRequests|[Parameters](#Parametersteams.scheduleCreateTimeOffRequests)|Not Found|
|[az teams team-schedule delete-offer-shift-request](#teams.scheduleDeleteOfferShiftRequests)|DeleteOfferShiftRequests|[Parameters](#Parametersteams.scheduleDeleteOfferShiftRequests)|Not Found|
|[az teams team-schedule delete-open-shift](#teams.scheduleDeleteOpenShifts)|DeleteOpenShifts|[Parameters](#Parametersteams.scheduleDeleteOpenShifts)|Not Found|
|[az teams team-schedule delete-open-shift-change-request](#teams.scheduleDeleteOpenShiftChangeRequests)|DeleteOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleDeleteOpenShiftChangeRequests)|Not Found|
|[az teams team-schedule delete-scheduling-group](#teams.scheduleDeleteSchedulingGroups)|DeleteSchedulingGroups|[Parameters](#Parametersteams.scheduleDeleteSchedulingGroups)|Not Found|
|[az teams team-schedule delete-shift](#teams.scheduleDeleteShifts)|DeleteShifts|[Parameters](#Parametersteams.scheduleDeleteShifts)|Not Found|
|[az teams team-schedule delete-swap-shift-change-request](#teams.scheduleDeleteSwapShiftsChangeRequests)|DeleteSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleDeleteSwapShiftsChangeRequests)|Not Found|
|[az teams team-schedule delete-time-card](#teams.scheduleDeleteTimeCards)|DeleteTimeCards|[Parameters](#Parametersteams.scheduleDeleteTimeCards)|Not Found|
|[az teams team-schedule delete-time-off](#teams.scheduleDeleteTimesOff)|DeleteTimesOff|[Parameters](#Parametersteams.scheduleDeleteTimesOff)|Not Found|
|[az teams team-schedule delete-time-off-reason](#teams.scheduleDeleteTimeOffReasons)|DeleteTimeOffReasons|[Parameters](#Parametersteams.scheduleDeleteTimeOffReasons)|Not Found|
|[az teams team-schedule delete-time-off-request](#teams.scheduleDeleteTimeOffRequests)|DeleteTimeOffRequests|[Parameters](#Parametersteams.scheduleDeleteTimeOffRequests)|Not Found|
|[az teams team-schedule list-offer-shift-request](#teams.scheduleListOfferShiftRequests)|ListOfferShiftRequests|[Parameters](#Parametersteams.scheduleListOfferShiftRequests)|Not Found|
|[az teams team-schedule list-open-shift](#teams.scheduleListOpenShifts)|ListOpenShifts|[Parameters](#Parametersteams.scheduleListOpenShifts)|Not Found|
|[az teams team-schedule list-open-shift-change-request](#teams.scheduleListOpenShiftChangeRequests)|ListOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleListOpenShiftChangeRequests)|Not Found|
|[az teams team-schedule list-scheduling-group](#teams.scheduleListSchedulingGroups)|ListSchedulingGroups|[Parameters](#Parametersteams.scheduleListSchedulingGroups)|Not Found|
|[az teams team-schedule list-shift](#teams.scheduleListShifts)|ListShifts|[Parameters](#Parametersteams.scheduleListShifts)|Not Found|
|[az teams team-schedule list-swap-shift-change-request](#teams.scheduleListSwapShiftsChangeRequests)|ListSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleListSwapShiftsChangeRequests)|Not Found|
|[az teams team-schedule list-time-card](#teams.scheduleListTimeCards)|ListTimeCards|[Parameters](#Parametersteams.scheduleListTimeCards)|Not Found|
|[az teams team-schedule list-time-off](#teams.scheduleListTimesOff)|ListTimesOff|[Parameters](#Parametersteams.scheduleListTimesOff)|Not Found|
|[az teams team-schedule list-time-off-reason](#teams.scheduleListTimeOffReasons)|ListTimeOffReasons|[Parameters](#Parametersteams.scheduleListTimeOffReasons)|Not Found|
|[az teams team-schedule list-time-off-request](#teams.scheduleListTimeOffRequests)|ListTimeOffRequests|[Parameters](#Parametersteams.scheduleListTimeOffRequests)|Not Found|
|[az teams team-schedule share](#teams.scheduleshare)|share|[Parameters](#Parametersteams.scheduleshare)|Not Found|
|[az teams team-schedule show-offer-shift-request](#teams.scheduleGetOfferShiftRequests)|GetOfferShiftRequests|[Parameters](#Parametersteams.scheduleGetOfferShiftRequests)|Not Found|
|[az teams team-schedule show-open-shift](#teams.scheduleGetOpenShifts)|GetOpenShifts|[Parameters](#Parametersteams.scheduleGetOpenShifts)|Not Found|
|[az teams team-schedule show-open-shift-change-request](#teams.scheduleGetOpenShiftChangeRequests)|GetOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleGetOpenShiftChangeRequests)|Not Found|
|[az teams team-schedule show-scheduling-group](#teams.scheduleGetSchedulingGroups)|GetSchedulingGroups|[Parameters](#Parametersteams.scheduleGetSchedulingGroups)|Not Found|
|[az teams team-schedule show-shift](#teams.scheduleGetShifts)|GetShifts|[Parameters](#Parametersteams.scheduleGetShifts)|Not Found|
|[az teams team-schedule show-swap-shift-change-request](#teams.scheduleGetSwapShiftsChangeRequests)|GetSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleGetSwapShiftsChangeRequests)|Not Found|
|[az teams team-schedule show-time-card](#teams.scheduleGetTimeCards)|GetTimeCards|[Parameters](#Parametersteams.scheduleGetTimeCards)|Not Found|
|[az teams team-schedule show-time-off](#teams.scheduleGetTimesOff)|GetTimesOff|[Parameters](#Parametersteams.scheduleGetTimesOff)|Not Found|
|[az teams team-schedule show-time-off-reason](#teams.scheduleGetTimeOffReasons)|GetTimeOffReasons|[Parameters](#Parametersteams.scheduleGetTimeOffReasons)|Not Found|
|[az teams team-schedule show-time-off-request](#teams.scheduleGetTimeOffRequests)|GetTimeOffRequests|[Parameters](#Parametersteams.scheduleGetTimeOffRequests)|Not Found|
|[az teams team-schedule update-offer-shift-request](#teams.scheduleUpdateOfferShiftRequests)|UpdateOfferShiftRequests|[Parameters](#Parametersteams.scheduleUpdateOfferShiftRequests)|Not Found|
|[az teams team-schedule update-open-shift](#teams.scheduleUpdateOpenShifts)|UpdateOpenShifts|[Parameters](#Parametersteams.scheduleUpdateOpenShifts)|Not Found|
|[az teams team-schedule update-open-shift-change-request](#teams.scheduleUpdateOpenShiftChangeRequests)|UpdateOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleUpdateOpenShiftChangeRequests)|Not Found|
|[az teams team-schedule update-scheduling-group](#teams.scheduleUpdateSchedulingGroups)|UpdateSchedulingGroups|[Parameters](#Parametersteams.scheduleUpdateSchedulingGroups)|Not Found|
|[az teams team-schedule update-shift](#teams.scheduleUpdateShifts)|UpdateShifts|[Parameters](#Parametersteams.scheduleUpdateShifts)|Not Found|
|[az teams team-schedule update-swap-shift-change-request](#teams.scheduleUpdateSwapShiftsChangeRequests)|UpdateSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleUpdateSwapShiftsChangeRequests)|Not Found|
|[az teams team-schedule update-time-card](#teams.scheduleUpdateTimeCards)|UpdateTimeCards|[Parameters](#Parametersteams.scheduleUpdateTimeCards)|Not Found|
|[az teams team-schedule update-time-off](#teams.scheduleUpdateTimesOff)|UpdateTimesOff|[Parameters](#Parametersteams.scheduleUpdateTimesOff)|Not Found|
|[az teams team-schedule update-time-off-reason](#teams.scheduleUpdateTimeOffReasons)|UpdateTimeOffReasons|[Parameters](#Parametersteams.scheduleUpdateTimeOffReasons)|Not Found|
|[az teams team-schedule update-time-off-request](#teams.scheduleUpdateTimeOffRequests)|UpdateTimeOffRequests|[Parameters](#Parametersteams.scheduleUpdateTimeOffRequests)|Not Found|

### <a name="CommandsInteams.schedule.timeCards">Commands in `az teams team-schedule-time-card` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team-schedule-time-card clock-in](#teams.schedule.timeCardsclockIn)|clockIn|[Parameters](#Parametersteams.schedule.timeCardsclockIn)|Not Found|
|[az teams team-schedule-time-card clock-out](#teams.schedule.timeCardsclockOut)|clockOut|[Parameters](#Parametersteams.schedule.timeCardsclockOut)|Not Found|
|[az teams team-schedule-time-card confirm](#teams.schedule.timeCardsconfirm)|confirm|[Parameters](#Parametersteams.schedule.timeCardsconfirm)|Not Found|
|[az teams team-schedule-time-card end-break](#teams.schedule.timeCardsendBreak)|endBreak|[Parameters](#Parametersteams.schedule.timeCardsendBreak)|Not Found|
|[az teams team-schedule-time-card start-break](#teams.schedule.timeCardsstartBreak)|startBreak|[Parameters](#Parametersteams.schedule.timeCardsstartBreak)|Not Found|

### <a name="CommandsInteamwork">Commands in `az teams teamwork` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamwork create-workforce-integration](#teamworkCreateWorkforceIntegrations)|CreateWorkforceIntegrations|[Parameters](#ParametersteamworkCreateWorkforceIntegrations)|Not Found|
|[az teams teamwork delete-workforce-integration](#teamworkDeleteWorkforceIntegrations)|DeleteWorkforceIntegrations|[Parameters](#ParametersteamworkDeleteWorkforceIntegrations)|Not Found|
|[az teams teamwork list-workforce-integration](#teamworkListWorkforceIntegrations)|ListWorkforceIntegrations|[Parameters](#ParametersteamworkListWorkforceIntegrations)|Not Found|
|[az teams teamwork show-workforce-integration](#teamworkGetWorkforceIntegrations)|GetWorkforceIntegrations|[Parameters](#ParametersteamworkGetWorkforceIntegrations)|Not Found|
|[az teams teamwork update-workforce-integration](#teamworkUpdateWorkforceIntegrations)|UpdateWorkforceIntegrations|[Parameters](#ParametersteamworkUpdateWorkforceIntegrations)|Not Found|

### <a name="CommandsInteamwork.teamwork">Commands in `az teams teamwork-teamwork` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamwork-teamwork show-teamwork](#teamwork.teamworkGetTeamwork)|GetTeamwork|[Parameters](#Parametersteamwork.teamworkGetTeamwork)|Not Found|
|[az teams teamwork-teamwork update-teamwork](#teamwork.teamworkUpdateTeamwork)|UpdateTeamwork|[Parameters](#Parametersteamwork.teamworkUpdateTeamwork)|Not Found|

### <a name="CommandsInusers">Commands in `az teams user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams user create-chat](#usersCreateChats)|CreateChats|[Parameters](#ParametersusersCreateChats)|Not Found|
|[az teams user create-joined-team](#usersCreateJoinedTeams)|CreateJoinedTeams|[Parameters](#ParametersusersCreateJoinedTeams)|Not Found|
|[az teams user delete-chat](#usersDeleteChats)|DeleteChats|[Parameters](#ParametersusersDeleteChats)|Not Found|
|[az teams user delete-joined-team](#usersDeleteJoinedTeams)|DeleteJoinedTeams|[Parameters](#ParametersusersDeleteJoinedTeams)|Not Found|
|[az teams user delete-teamwork](#usersDeleteTeamwork)|DeleteTeamwork|[Parameters](#ParametersusersDeleteTeamwork)|Not Found|
|[az teams user list-chat](#usersListChats)|ListChats|[Parameters](#ParametersusersListChats)|Not Found|
|[az teams user list-joined-team](#usersListJoinedTeams)|ListJoinedTeams|[Parameters](#ParametersusersListJoinedTeams)|Not Found|
|[az teams user show-chat](#usersGetChats)|GetChats|[Parameters](#ParametersusersGetChats)|Not Found|
|[az teams user show-joined-team](#usersGetJoinedTeams)|GetJoinedTeams|[Parameters](#ParametersusersGetJoinedTeams)|Not Found|
|[az teams user show-teamwork](#usersGetTeamwork)|GetTeamwork|[Parameters](#ParametersusersGetTeamwork)|Not Found|
|[az teams user update-chat](#usersUpdateChats)|UpdateChats|[Parameters](#ParametersusersUpdateChats)|Not Found|
|[az teams user update-joined-team](#usersUpdateJoinedTeams)|UpdateJoinedTeams|[Parameters](#ParametersusersUpdateJoinedTeams)|Not Found|
|[az teams user update-teamwork](#usersUpdateTeamwork)|UpdateTeamwork|[Parameters](#ParametersusersUpdateTeamwork)|Not Found|

### <a name="CommandsInusers.teamwork">Commands in `az teams user-teamwork` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams user-teamwork create-installed-app](#users.teamworkCreateInstalledApps)|CreateInstalledApps|[Parameters](#Parametersusers.teamworkCreateInstalledApps)|Not Found|
|[az teams user-teamwork delete-installed-app](#users.teamworkDeleteInstalledApps)|DeleteInstalledApps|[Parameters](#Parametersusers.teamworkDeleteInstalledApps)|Not Found|
|[az teams user-teamwork list-installed-app](#users.teamworkListInstalledApps)|ListInstalledApps|[Parameters](#Parametersusers.teamworkListInstalledApps)|Not Found|
|[az teams user-teamwork show-installed-app](#users.teamworkGetInstalledApps)|GetInstalledApps|[Parameters](#Parametersusers.teamworkGetInstalledApps)|Not Found|
|[az teams user-teamwork update-installed-app](#users.teamworkUpdateInstalledApps)|UpdateInstalledApps|[Parameters](#Parametersusers.teamworkUpdateInstalledApps)|Not Found|

### <a name="CommandsInusers.teamwork.installedApps">Commands in `az teams user-teamwork-installed-app` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams user-teamwork-installed-app delete-ref-chat](#users.teamwork.installedAppsDeleteRefChat)|DeleteRefChat|[Parameters](#Parametersusers.teamwork.installedAppsDeleteRefChat)|Not Found|
|[az teams user-teamwork-installed-app set-ref-chat](#users.teamwork.installedAppsSetRefChat)|SetRefChat|[Parameters](#Parametersusers.teamwork.installedAppsSetRefChat)|Not Found|
|[az teams user-teamwork-installed-app show-chat](#users.teamwork.installedAppsGetChat)|GetChat|[Parameters](#Parametersusers.teamwork.installedAppsGetChat)|Not Found|
|[az teams user-teamwork-installed-app show-ref-chat](#users.teamwork.installedAppsGetRefChat)|GetRefChat|[Parameters](#Parametersusers.teamwork.installedAppsGetRefChat)|Not Found|


## COMMAND DETAILS

### group `az teams app-catalog`
#### <a name="appCatalogsCreateTeamsApps">Command `az teams app-catalog create-team-app`</a>

##### <a name="ParametersappCatalogsCreateTeamsApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="appCatalogsDeleteTeamsApps">Command `az teams app-catalog delete-team-app`</a>

##### <a name="ParametersappCatalogsDeleteTeamsApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--teams-app-id**|string|key: id of teamsApp|teams_app_id|teamsApp-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="appCatalogsListTeamsApps">Command `az teams app-catalog list-team-app`</a>

##### <a name="ParametersappCatalogsListTeamsApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="appCatalogsGetTeamsApps">Command `az teams app-catalog show-team-app`</a>

##### <a name="ParametersappCatalogsGetTeamsApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--teams-app-id**|string|key: id of teamsApp|teams_app_id|teamsApp-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="appCatalogsUpdateTeamsApps">Command `az teams app-catalog update-team-app`</a>

##### <a name="ParametersappCatalogsUpdateTeamsApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--teams-app-id**|string|key: id of teamsApp|teams_app_id|teamsApp-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### group `az teams app-catalog-team-app`
#### <a name="appCatalogs.teamsAppsCreateAppDefinitions">Command `az teams app-catalog-team-app create-app-definition`</a>

##### <a name="ParametersappCatalogs.teamsAppsCreateAppDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--teams-app-id**|string|key: id of teamsApp|teams_app_id|teamsApp-id|
|**--id**|string|Read-only.|id|id|
|**--azure-ad-app-id**|string||azure_ad_app_id|azureADAppId|
|**--description**|string||description|description|
|**--display-name**|string|The name of the app provided by the app developer.|display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--shortdescription**|string||shortdescription|shortdescription|
|**--microsoft-graph-teams-app-definition-teams-app-id-teams-app-id**|string|The ID from the Teams app manifest.|microsoft_graph_teams_app_definition_teams_app_id_teams_app_id|teamsAppId|
|**--version**|string|The version number of the application.|version|version|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="appCatalogs.teamsAppsDeleteAppDefinitions">Command `az teams app-catalog-team-app delete-app-definition`</a>

##### <a name="ParametersappCatalogs.teamsAppsDeleteAppDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--teams-app-id**|string|key: id of teamsApp|teams_app_id|teamsApp-id|
|**--teams-app-definition-id**|string|key: id of teamsAppDefinition|teams_app_definition_id|teamsAppDefinition-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="appCatalogs.teamsAppsListAppDefinitions">Command `az teams app-catalog-team-app list-app-definition`</a>

##### <a name="ParametersappCatalogs.teamsAppsListAppDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--teams-app-id**|string|key: id of teamsApp|teams_app_id|teamsApp-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="appCatalogs.teamsAppsGetAppDefinitions">Command `az teams app-catalog-team-app show-app-definition`</a>

##### <a name="ParametersappCatalogs.teamsAppsGetAppDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--teams-app-id**|string|key: id of teamsApp|teams_app_id|teamsApp-id|
|**--teams-app-definition-id**|string|key: id of teamsAppDefinition|teams_app_definition_id|teamsAppDefinition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="appCatalogs.teamsAppsUpdateAppDefinitions">Command `az teams app-catalog-team-app update-app-definition`</a>

##### <a name="ParametersappCatalogs.teamsAppsUpdateAppDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--teams-app-id**|string|key: id of teamsApp|teams_app_id|teamsApp-id|
|**--teams-app-definition-id**|string|key: id of teamsAppDefinition|teams_app_definition_id|teamsAppDefinition-id|
|**--id**|string|Read-only.|id|id|
|**--azure-ad-app-id**|string||azure_ad_app_id|azureADAppId|
|**--description**|string||description|description|
|**--display-name**|string|The name of the app provided by the app developer.|display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--shortdescription**|string||shortdescription|shortdescription|
|**--microsoft-graph-teams-app-definition-teams-app-id-teams-app-id**|string|The ID from the Teams app manifest.|microsoft_graph_teams_app_definition_teams_app_id_teams_app_id|teamsAppId|
|**--version**|string|The version number of the application.|version|version|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

### group `az teams chat`
#### <a name="chatsallMessages">Command `az teams chat all-message`</a>

##### <a name="ParameterschatsallMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="chatsCreateInstalledApps">Command `az teams chat create-installed-app`</a>

##### <a name="ParameterschatsCreateInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--azure-ad-app-id**|string||azure_ad_app_id|azureADAppId|
|**--description**|string||description|description|
|**--display-name**|string|The name of the app provided by the app developer.|display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--shortdescription**|string||shortdescription|shortdescription|
|**--teams-app-id**|string|The ID from the Teams app manifest.|teams_app_id|teamsAppId|
|**--version**|string|The version number of the application.|version|version|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--id1**|string|Read-only.|id1|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="chatsCreateMembers">Command `az teams chat create-member`</a>

##### <a name="ParameterschatsCreateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="chatsCreateMessages">Command `az teams chat create-message`</a>

##### <a name="ParameterschatsCreateMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--microsoft-graph-chat-message-chat-id**|string||microsoft_graph_chat_message_chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="chatsCreateTabs">Command `az teams chat create-tab`</a>

##### <a name="ParameterschatsCreateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--message-id**|string||message_id|messageId|
|**--sort-order-index**|string||sort_order_index|sortOrderIndex|
|**--teams-app-id**|string||teams_app_id|teamsAppId|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="chatsDeleteInstalledApps">Command `az teams chat delete-installed-app`</a>

##### <a name="ParameterschatsDeleteInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chatsDeleteMembers">Command `az teams chat delete-member`</a>

##### <a name="ParameterschatsDeleteMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chatsDeleteMessages">Command `az teams chat delete-message`</a>

##### <a name="ParameterschatsDeleteMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chatsDeleteTabs">Command `az teams chat delete-tab`</a>

##### <a name="ParameterschatsDeleteTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chatsListInstalledApps">Command `az teams chat list-installed-app`</a>

##### <a name="ParameterschatsListInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chatsListMembers">Command `az teams chat list-member`</a>

##### <a name="ParameterschatsListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chatsListMessages">Command `az teams chat list-message`</a>

##### <a name="ParameterschatsListMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chatsListTabs">Command `az teams chat list-tab`</a>

##### <a name="ParameterschatsListTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chatssendActivityNotification">Command `az teams chat send-activity-notification`</a>

##### <a name="ParameterschatssendActivityNotification">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--topic**|object|teamworkActivityTopic|topic|topic|
|**--activity-type**|string||activity_type|activityType|
|**--chain-id**|integer||chain_id|chainId|
|**--preview-text**|object|itemBody|preview_text|previewText|
|**--template-parameters**|array||template_parameters|templateParameters|
|**--recipient**|dictionary|teamworkNotificationRecipient|recipient|recipient|

#### <a name="chatsgetAllMessages">Command `az teams chat show-all-message`</a>

##### <a name="ParameterschatsgetAllMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="chatsGetInstalledApps">Command `az teams chat show-installed-app`</a>

##### <a name="ParameterschatsGetInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chatsGetMembers">Command `az teams chat show-member`</a>

##### <a name="ParameterschatsGetMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chatsGetMessages">Command `az teams chat show-message`</a>

##### <a name="ParameterschatsGetMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chatsGetTabs">Command `az teams chat show-tab`</a>

##### <a name="ParameterschatsGetTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chatsUpdateInstalledApps">Command `az teams chat update-installed-app`</a>

##### <a name="ParameterschatsUpdateInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--azure-ad-app-id**|string||azure_ad_app_id|azureADAppId|
|**--description**|string||description|description|
|**--display-name**|string|The name of the app provided by the app developer.|display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--shortdescription**|string||shortdescription|shortdescription|
|**--teams-app-id**|string|The ID from the Teams app manifest.|teams_app_id|teamsAppId|
|**--version**|string|The version number of the application.|version|version|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--id1**|string|Read-only.|id1|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="chatsUpdateMembers">Command `az teams chat update-member`</a>

##### <a name="ParameterschatsUpdateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="chatsUpdateMessages">Command `az teams chat update-message`</a>

##### <a name="ParameterschatsUpdateMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--microsoft-graph-chat-message-chat-id**|string||microsoft_graph_chat_message_chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="chatsUpdateTabs">Command `az teams chat update-tab`</a>

##### <a name="ParameterschatsUpdateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--message-id**|string||message_id|messageId|
|**--sort-order-index**|string||sort_order_index|sortOrderIndex|
|**--teams-app-id**|string||teams_app_id|teamsAppId|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### group `az teams chat-chat`
#### <a name="chats.chatCreateChat">Command `az teams chat-chat create-chat`</a>

##### <a name="Parameterschats.chatCreateChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--topic**|string||topic|topic|
|**--installed-apps**|array||installed_apps|installedApps|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--tabs**|array||tabs|tabs|

#### <a name="chats.chatDeleteChat">Command `az teams chat-chat delete-chat`</a>

##### <a name="Parameterschats.chatDeleteChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chats.chatListChat">Command `az teams chat-chat list-chat`</a>

##### <a name="Parameterschats.chatListChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.chatGetChat">Command `az teams chat-chat show-chat`</a>

##### <a name="Parameterschats.chatGetChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.chatUpdateChat">Command `az teams chat-chat update-chat`</a>

##### <a name="Parameterschats.chatUpdateChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--topic**|string||topic|topic|
|**--installed-apps**|array||installed_apps|installedApps|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--tabs**|array||tabs|tabs|

### group `az teams chat-installed-app`
#### <a name="chats.installedAppsDeleteRefTeamsApp">Command `az teams chat-installed-app delete-ref-team-app`</a>

##### <a name="Parameterschats.installedAppsDeleteRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chats.installedAppsDeleteRefTeamsAppDefinition">Command `az teams chat-installed-app delete-ref-team-app-definition`</a>

##### <a name="Parameterschats.installedAppsDeleteRefTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chats.installedAppsSetRefTeamsApp">Command `az teams chat-installed-app set-ref-team-app`</a>

##### <a name="Parameterschats.installedAppsSetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="chats.installedAppsSetRefTeamsAppDefinition">Command `az teams chat-installed-app set-ref-team-app-definition`</a>

##### <a name="Parameterschats.installedAppsSetRefTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="chats.installedAppsGetRefTeamsApp">Command `az teams chat-installed-app show-ref-team-app`</a>

##### <a name="Parameterschats.installedAppsGetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

#### <a name="chats.installedAppsGetRefTeamsAppDefinition">Command `az teams chat-installed-app show-ref-team-app-definition`</a>

##### <a name="Parameterschats.installedAppsGetRefTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

#### <a name="chats.installedAppsGetTeamsApp">Command `az teams chat-installed-app show-team-app`</a>

##### <a name="Parameterschats.installedAppsGetTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.installedAppsGetTeamsAppDefinition">Command `az teams chat-installed-app show-team-app-definition`</a>

##### <a name="Parameterschats.installedAppsGetTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.installedAppsupgrade">Command `az teams chat-installed-app upgrade`</a>

##### <a name="Parameterschats.installedAppsupgrade">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

### group `az teams chat-member`
#### <a name="chats.membersadd">Command `az teams chat-member add`</a>

##### <a name="Parameterschats.membersadd">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--values**|array||values|values|

### group `az teams chat-message`
#### <a name="chats.messagesCreateHostedContents">Command `az teams chat-message create-hosted-content`</a>

##### <a name="Parameterschats.messagesCreateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--content-bytes**|byte-array||content_bytes|contentBytes|
|**--content-type**|string||content_type|contentType|

#### <a name="chats.messagesCreateReplies">Command `az teams chat-message create-reply`</a>

##### <a name="Parameterschats.messagesCreateReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--microsoft-graph-chat-message-chat-id**|string||microsoft_graph_chat_message_chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="chats.messagesDeleteHostedContents">Command `az teams chat-message delete-hosted-content`</a>

##### <a name="Parameterschats.messagesDeleteHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chats.messagesDeleteReplies">Command `az teams chat-message delete-reply`</a>

##### <a name="Parameterschats.messagesDeleteReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chats.messagesdelta">Command `az teams chat-message delta`</a>

##### <a name="Parameterschats.messagesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|

#### <a name="chats.messagesListHostedContents">Command `az teams chat-message list-hosted-content`</a>

##### <a name="Parameterschats.messagesListHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.messagesListReplies">Command `az teams chat-message list-reply`</a>

##### <a name="Parameterschats.messagesListReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.messagesSetHostedContentsContent">Command `az teams chat-message set-hosted-content-content`</a>

##### <a name="Parameterschats.messagesSetHostedContentsContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--data**|binary|New media content.|data|data|

#### <a name="chats.messagesGetHostedContents">Command `az teams chat-message show-hosted-content`</a>

##### <a name="Parameterschats.messagesGetHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.messagesGetHostedContentsContent">Command `az teams chat-message show-hosted-content-content`</a>

##### <a name="Parameterschats.messagesGetHostedContentsContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|

#### <a name="chats.messagesGetReplies">Command `az teams chat-message show-reply`</a>

##### <a name="Parameterschats.messagesGetReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.messagesUpdateHostedContents">Command `az teams chat-message update-hosted-content`</a>

##### <a name="Parameterschats.messagesUpdateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--id**|string|Read-only.|id|id|
|**--content-bytes**|byte-array||content_bytes|contentBytes|
|**--content-type**|string||content_type|contentType|

#### <a name="chats.messagesUpdateReplies">Command `az teams chat-message update-reply`</a>

##### <a name="Parameterschats.messagesUpdateReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--microsoft-graph-chat-message-chat-id**|string||microsoft_graph_chat_message_chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

### group `az teams chat-message-reply`
#### <a name="chats.messages.repliesdelta">Command `az teams chat-message-reply delta`</a>

##### <a name="Parameterschats.messages.repliesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|

### group `az teams chat-tab`
#### <a name="chats.tabsDeleteRefTeamsApp">Command `az teams chat-tab delete-ref-team-app`</a>

##### <a name="Parameterschats.tabsDeleteRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chats.tabsSetRefTeamsApp">Command `az teams chat-tab set-ref-team-app`</a>

##### <a name="Parameterschats.tabsSetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="chats.tabsGetRefTeamsApp">Command `az teams chat-tab show-ref-team-app`</a>

##### <a name="Parameterschats.tabsGetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|

#### <a name="chats.tabsGetTeamsApp">Command `az teams chat-tab show-team-app`</a>

##### <a name="Parameterschats.tabsGetTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az teams group`
#### <a name="groupsDeleteTeam">Command `az teams group delete-team`</a>

##### <a name="ParametersgroupsDeleteTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsGetTeam">Command `az teams group show-team`</a>

##### <a name="ParametersgroupsGetTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsUpdateTeam">Command `az teams group update-team`</a>

##### <a name="ParametersgroupsUpdateTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--is-membership-limited-to-owners**|boolean||is_membership_limited_to_owners|isMembershipLimitedToOwners|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--owners**|array||owners|owners|
|**--photo**|object|profilePhoto|photo|photo|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--provision-status**|choice||provision_status|provisionStatus|
|**--provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--open-shifts**|array||open_shifts|openShifts|
|**--scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--time-cards**|array||time_cards|timeCards|
|**--time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--time-off-requests**|array||time_off_requests|timeOffRequests|
|**--times-off**|array|The instances of times off in the schedule.|times_off|timesOff|
|**--approved-location**|object|geoCoordinates|approved_location|approvedLocation|
|**--show-in-teams-search-and-suggestions**|boolean||show_in_teams_search_and_suggestions|showInTeamsSearchAndSuggestions|

### group `az teams team`
#### <a name="teams.teamListTeam">Command `az teams team list`</a>

##### <a name="Parametersteams.teamListTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.teamCreateTeam">Command `az teams team create`</a>

##### <a name="Parametersteams.teamCreateTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--is-membership-limited-to-owners**|boolean||is_membership_limited_to_owners|isMembershipLimitedToOwners|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--owners**|array||owners|owners|
|**--photo**|object|profilePhoto|photo|photo|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--provision-status**|choice||provision_status|provisionStatus|
|**--provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--open-shifts**|array||open_shifts|openShifts|
|**--scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--time-cards**|array||time_cards|timeCards|
|**--time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--time-off-requests**|array||time_off_requests|timeOffRequests|
|**--times-off**|array|The instances of times off in the schedule.|times_off|timesOff|
|**--approved-location**|object|geoCoordinates|approved_location|approvedLocation|
|**--show-in-teams-search-and-suggestions**|boolean||show_in_teams_search_and_suggestions|showInTeamsSearchAndSuggestions|

#### <a name="teams.teamUpdateTeam">Command `az teams team update`</a>

##### <a name="Parametersteams.teamUpdateTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--is-membership-limited-to-owners**|boolean||is_membership_limited_to_owners|isMembershipLimitedToOwners|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--owners**|array||owners|owners|
|**--photo**|object|profilePhoto|photo|photo|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--provision-status**|choice||provision_status|provisionStatus|
|**--provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--open-shifts**|array||open_shifts|openShifts|
|**--scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--time-cards**|array||time_cards|timeCards|
|**--time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--time-off-requests**|array||time_off_requests|timeOffRequests|
|**--times-off**|array|The instances of times off in the schedule.|times_off|timesOff|
|**--approved-location**|object|geoCoordinates|approved_location|approvedLocation|
|**--show-in-teams-search-and-suggestions**|boolean||show_in_teams_search_and_suggestions|showInTeamsSearchAndSuggestions|

#### <a name="teams.teamDeleteTeam">Command `az teams team delete-team`</a>

##### <a name="Parametersteams.teamDeleteTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.teamGetTeam">Command `az teams team show-team`</a>

##### <a name="Parametersteams.teamGetTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az teams team`
#### <a name="teamsallMessages">Command `az teams team all-message`</a>

##### <a name="ParametersteamsallMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="teamsarchive">Command `az teams team archive`</a>

##### <a name="Parametersteamsarchive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--should-set-spo-site-read-only-for-members**|boolean||should_set_spo_site_read_only_for_members|shouldSetSpoSiteReadOnlyForMembers|

#### <a name="teamsclone">Command `az teams team clone`</a>

##### <a name="Parametersteamsclone">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--display-name**|string||display_name|displayName|
|**--description**|string||description|description|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--classification**|string||classification|classification|
|**--visibility**|choice||visibility|visibility|
|**--parts-to-clone**|choice||parts_to_clone|partsToClone|

#### <a name="teamscompleteMigration">Command `az teams team complete-migration`</a>

##### <a name="ParametersteamscompleteMigration">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teamsCreateChannels">Command `az teams team create-channel`</a>

##### <a name="ParametersteamsCreateChannels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read only. Timestamp at which the channel was created.|created_date_time|createdDateTime|
|**--description**|string|Optional textual description for the channel.|description|description|
|**--display-name**|string|Channel name as it will appear to the user in Microsoft Teams.|display_name|displayName|
|**--email**|string|The email address for sending messages to the channel. Read-only.|email|email|
|**--is-favorite-by-default**|boolean|Indicates whether the channel should automatically be marked 'favorite' for all members of the team. Can only be set programmatically with Create team. Default: false.|is_favorite_by_default|isFavoriteByDefault|
|**--membership-type**|choice||membership_type|membershipType|
|**--moderation-settings**|object|channelModerationSettings|moderation_settings|moderationSettings|
|**--web-url**|string|A hyperlink that will go to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.|web_url|webUrl|
|**--files-folder**|object|driveItem|files_folder|filesFolder|
|**--members**|array||members|members|
|**--messages**|array|A collection of all the messages in the channel. A navigation property. Nullable.|messages|messages|
|**--tabs**|array|A collection of all the tabs in the channel. A navigation property.|tabs|tabs|

#### <a name="teamsCreateInstalledApps">Command `az teams team create-installed-app`</a>

##### <a name="ParametersteamsCreateInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--azure-ad-app-id**|string||azure_ad_app_id|azureADAppId|
|**--description**|string||description|description|
|**--display-name**|string|The name of the app provided by the app developer.|display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--shortdescription**|string||shortdescription|shortdescription|
|**--teams-app-id**|string|The ID from the Teams app manifest.|teams_app_id|teamsAppId|
|**--version**|string|The version number of the application.|version|version|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--id1**|string|Read-only.|id1|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="teamsCreateMembers">Command `az teams team create-member`</a>

##### <a name="ParametersteamsCreateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teamsCreateOperations">Command `az teams team create-operation`</a>

##### <a name="ParametersteamsCreateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--attempts-count**|integer|Number of times the operation was attempted before being marked successful or failed.|attempts_count|attemptsCount|
|**--created-date-time**|date-time|Time when the operation was created.|created_date_time|createdDateTime|
|**--error**|object|operationError|error|error|
|**--last-action-date-time**|date-time|Time when the async operation was last updated.|last_action_date_time|lastActionDateTime|
|**--operation-type**|choice||operation_type|operationType|
|**--status**|choice||status|status|
|**--target-resource-id**|string|The ID of the object that's created or modified as result of this async operation, typically a team.|target_resource_id|targetResourceId|
|**--target-resource-location**|string|The location of the object that's created or modified as result of this async operation. This URL should be treated as an opaque value and not parsed into its component paths.|target_resource_location|targetResourceLocation|

#### <a name="teamsCreateRefOwners">Command `az teams team create-ref-owner`</a>

##### <a name="ParametersteamsCreateRefOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="teamsDeleteChannels">Command `az teams team delete-channel`</a>

##### <a name="ParametersteamsDeleteChannels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteInstalledApps">Command `az teams team delete-installed-app`</a>

##### <a name="ParametersteamsDeleteInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteMembers">Command `az teams team delete-member`</a>

##### <a name="ParametersteamsDeleteMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteOperations">Command `az teams team delete-operation`</a>

##### <a name="ParametersteamsDeleteOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-async-operation-id**|string|key: id of teamsAsyncOperation|teams_async_operation_id|teamsAsyncOperation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeletePhoto">Command `az teams team delete-photo`</a>

##### <a name="ParametersteamsDeletePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeletePrimaryChannel">Command `az teams team delete-primary-channel`</a>

##### <a name="ParametersteamsDeletePrimaryChannel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteRefGroup">Command `az teams team delete-ref-group`</a>

##### <a name="ParametersteamsDeleteRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteRefTemplate">Command `az teams team delete-ref-template`</a>

##### <a name="ParametersteamsDeleteRefTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteSchedule">Command `az teams team delete-schedule`</a>

##### <a name="ParametersteamsDeleteSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsListChannels">Command `az teams team list-channel`</a>

##### <a name="ParametersteamsListChannels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsListInstalledApps">Command `az teams team list-installed-app`</a>

##### <a name="ParametersteamsListInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsListMembers">Command `az teams team list-member`</a>

##### <a name="ParametersteamsListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsListOperations">Command `az teams team list-operation`</a>

##### <a name="ParametersteamsListOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsListOwners">Command `az teams team list-owner`</a>

##### <a name="ParametersteamsListOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsListRefOwners">Command `az teams team list-ref-owner`</a>

##### <a name="ParametersteamsListRefOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="teamssendActivityNotification">Command `az teams team send-activity-notification`</a>

##### <a name="ParametersteamssendActivityNotification">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--topic**|object|teamworkActivityTopic|topic|topic|
|**--activity-type**|string||activity_type|activityType|
|**--chain-id**|integer||chain_id|chainId|
|**--preview-text**|object|itemBody|preview_text|previewText|
|**--template-parameters**|array||template_parameters|templateParameters|
|**--recipient**|dictionary|teamworkNotificationRecipient|recipient|recipient|

#### <a name="teamsSetPhotoContent">Command `az teams team set-photo-content`</a>

##### <a name="ParametersteamsSetPhotoContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--data**|binary|New media content.|data|data|

#### <a name="teamsSetRefGroup">Command `az teams team set-ref-group`</a>

##### <a name="ParametersteamsSetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teamsSetRefTemplate">Command `az teams team set-ref-template`</a>

##### <a name="ParametersteamsSetRefTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teamsgetAllMessages">Command `az teams team show-all-message`</a>

##### <a name="ParametersteamsgetAllMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="teamsGetChannels">Command `az teams team show-channel`</a>

##### <a name="ParametersteamsGetChannels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetGroup">Command `az teams team show-group`</a>

##### <a name="ParametersteamsGetGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetInstalledApps">Command `az teams team show-installed-app`</a>

##### <a name="ParametersteamsGetInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetMembers">Command `az teams team show-member`</a>

##### <a name="ParametersteamsGetMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetOperations">Command `az teams team show-operation`</a>

##### <a name="ParametersteamsGetOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-async-operation-id**|string|key: id of teamsAsyncOperation|teams_async_operation_id|teamsAsyncOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetPhoto">Command `az teams team show-photo`</a>

##### <a name="ParametersteamsGetPhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetPhotoContent">Command `az teams team show-photo-content`</a>

##### <a name="ParametersteamsGetPhotoContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teamsGetPrimaryChannel">Command `az teams team show-primary-channel`</a>

##### <a name="ParametersteamsGetPrimaryChannel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetRefGroup">Command `az teams team show-ref-group`</a>

##### <a name="ParametersteamsGetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teamsGetRefTemplate">Command `az teams team show-ref-template`</a>

##### <a name="ParametersteamsGetRefTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teamsGetSchedule">Command `az teams team show-schedule`</a>

##### <a name="ParametersteamsGetSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetTemplate">Command `az teams team show-template`</a>

##### <a name="ParametersteamsGetTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsunarchive">Command `az teams team unarchive`</a>

##### <a name="Parametersteamsunarchive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teamsUpdateChannels">Command `az teams team update-channel`</a>

##### <a name="ParametersteamsUpdateChannels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read only. Timestamp at which the channel was created.|created_date_time|createdDateTime|
|**--description**|string|Optional textual description for the channel.|description|description|
|**--display-name**|string|Channel name as it will appear to the user in Microsoft Teams.|display_name|displayName|
|**--email**|string|The email address for sending messages to the channel. Read-only.|email|email|
|**--is-favorite-by-default**|boolean|Indicates whether the channel should automatically be marked 'favorite' for all members of the team. Can only be set programmatically with Create team. Default: false.|is_favorite_by_default|isFavoriteByDefault|
|**--membership-type**|choice||membership_type|membershipType|
|**--moderation-settings**|object|channelModerationSettings|moderation_settings|moderationSettings|
|**--web-url**|string|A hyperlink that will go to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.|web_url|webUrl|
|**--files-folder**|object|driveItem|files_folder|filesFolder|
|**--members**|array||members|members|
|**--messages**|array|A collection of all the messages in the channel. A navigation property. Nullable.|messages|messages|
|**--tabs**|array|A collection of all the tabs in the channel. A navigation property.|tabs|tabs|

#### <a name="teamsUpdateInstalledApps">Command `az teams team update-installed-app`</a>

##### <a name="ParametersteamsUpdateInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--azure-ad-app-id**|string||azure_ad_app_id|azureADAppId|
|**--description**|string||description|description|
|**--display-name**|string|The name of the app provided by the app developer.|display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--shortdescription**|string||shortdescription|shortdescription|
|**--teams-app-id**|string|The ID from the Teams app manifest.|teams_app_id|teamsAppId|
|**--version**|string|The version number of the application.|version|version|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--id1**|string|Read-only.|id1|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="teamsUpdateMembers">Command `az teams team update-member`</a>

##### <a name="ParametersteamsUpdateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teamsUpdateOperations">Command `az teams team update-operation`</a>

##### <a name="ParametersteamsUpdateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-async-operation-id**|string|key: id of teamsAsyncOperation|teams_async_operation_id|teamsAsyncOperation-id|
|**--id**|string|Read-only.|id|id|
|**--attempts-count**|integer|Number of times the operation was attempted before being marked successful or failed.|attempts_count|attemptsCount|
|**--created-date-time**|date-time|Time when the operation was created.|created_date_time|createdDateTime|
|**--error**|object|operationError|error|error|
|**--last-action-date-time**|date-time|Time when the async operation was last updated.|last_action_date_time|lastActionDateTime|
|**--operation-type**|choice||operation_type|operationType|
|**--status**|choice||status|status|
|**--target-resource-id**|string|The ID of the object that's created or modified as result of this async operation, typically a team.|target_resource_id|targetResourceId|
|**--target-resource-location**|string|The location of the object that's created or modified as result of this async operation. This URL should be treated as an opaque value and not parsed into its component paths.|target_resource_location|targetResourceLocation|

#### <a name="teamsUpdatePhoto">Command `az teams team update-photo`</a>

##### <a name="ParametersteamsUpdatePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

#### <a name="teamsUpdatePrimaryChannel">Command `az teams team update-primary-channel`</a>

##### <a name="ParametersteamsUpdatePrimaryChannel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Read only. Timestamp at which the channel was created.|created_date_time|createdDateTime|
|**--description**|string|Optional textual description for the channel.|description|description|
|**--display-name**|string|Channel name as it will appear to the user in Microsoft Teams.|display_name|displayName|
|**--email**|string|The email address for sending messages to the channel. Read-only.|email|email|
|**--is-favorite-by-default**|boolean|Indicates whether the channel should automatically be marked 'favorite' for all members of the team. Can only be set programmatically with Create team. Default: false.|is_favorite_by_default|isFavoriteByDefault|
|**--membership-type**|choice||membership_type|membershipType|
|**--moderation-settings**|object|channelModerationSettings|moderation_settings|moderationSettings|
|**--web-url**|string|A hyperlink that will go to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.|web_url|webUrl|
|**--files-folder**|object|driveItem|files_folder|filesFolder|
|**--members**|array||members|members|
|**--messages**|array|A collection of all the messages in the channel. A navigation property. Nullable.|messages|messages|
|**--tabs**|array|A collection of all the tabs in the channel. A navigation property.|tabs|tabs|

#### <a name="teamsUpdateSchedule">Command `az teams team update-schedule`</a>

##### <a name="ParametersteamsUpdateSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--provision-status**|choice||provision_status|provisionStatus|
|**--provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--open-shifts**|array||open_shifts|openShifts|
|**--scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--time-cards**|array||time_cards|timeCards|
|**--time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--time-off-requests**|array||time_off_requests|timeOffRequests|
|**--times-off**|array|The instances of times off in the schedule.|times_off|timesOff|
|**--approved-location**|object|geoCoordinates|approved_location|approvedLocation|

### group `az teams team-channel`
#### <a name="teams.channelsallMessages">Command `az teams team-channel all-message`</a>

##### <a name="Parametersteams.channelsallMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teams.channelscompleteMigration">Command `az teams team-channel complete-migration`</a>

##### <a name="Parametersteams.channelscompleteMigration">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|

#### <a name="teams.channelsCreateMembers">Command `az teams team-channel create-member`</a>

##### <a name="Parametersteams.channelsCreateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teams.channelsCreateMessages">Command `az teams team-channel create-message`</a>

##### <a name="Parametersteams.channelsCreateMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--chat-id**|string||chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.channelsCreateTabs">Command `az teams team-channel create-tab`</a>

##### <a name="Parametersteams.channelsCreateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--message-id**|string||message_id|messageId|
|**--sort-order-index**|string||sort_order_index|sortOrderIndex|
|**--teams-app-id**|string||teams_app_id|teamsAppId|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="teams.channelsDeleteFilesFolder">Command `az teams team-channel delete-file-folder`</a>

##### <a name="Parametersteams.channelsDeleteFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channelsDeleteMembers">Command `az teams team-channel delete-member`</a>

##### <a name="Parametersteams.channelsDeleteMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channelsDeleteMessages">Command `az teams team-channel delete-message`</a>

##### <a name="Parametersteams.channelsDeleteMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channelsDeleteTabs">Command `az teams team-channel delete-tab`</a>

##### <a name="Parametersteams.channelsDeleteTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channelsListMembers">Command `az teams team-channel list-member`</a>

##### <a name="Parametersteams.channelsListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsListMessages">Command `az teams team-channel list-message`</a>

##### <a name="Parametersteams.channelsListMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsListTabs">Command `az teams team-channel list-tab`</a>

##### <a name="Parametersteams.channelsListTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsSetFilesFolderContent">Command `az teams team-channel set-file-folder-content`</a>

##### <a name="Parametersteams.channelsSetFilesFolderContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--data**|binary|New media content.|data|data|

#### <a name="teams.channelsGetFilesFolder">Command `az teams team-channel show-file-folder`</a>

##### <a name="Parametersteams.channelsGetFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsGetFilesFolderContent">Command `az teams team-channel show-file-folder-content`</a>

##### <a name="Parametersteams.channelsGetFilesFolderContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|

#### <a name="teams.channelsGetMembers">Command `az teams team-channel show-member`</a>

##### <a name="Parametersteams.channelsGetMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsGetMessages">Command `az teams team-channel show-message`</a>

##### <a name="Parametersteams.channelsGetMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsGetTabs">Command `az teams team-channel show-tab`</a>

##### <a name="Parametersteams.channelsGetTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsUpdateFilesFolder">Command `az teams team-channel update-file-folder`</a>

##### <a name="Parametersteams.channelsUpdateFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--list-item**|object|listItem|list_item|listItem|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--all-time**|object|itemActivityStat|all_time|allTime|
|**--item-activity-stats**|array||item_activity_stats|itemActivityStats|
|**--last-seven-days**|object|itemActivityStat|last_seven_days|lastSevenDays|
|**--id1**|string|Read-only.|id1|id|
|**--microsoft-graph-workbook-application**|object|workbookApplication|microsoft_graph_workbook_application|application|
|**--comments**|array||comments|comments|
|**--functions**|object|workbookFunctions|functions|functions|
|**--names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--microsoft-graph-special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--owner**|object|identitySet|owner|owner|
|**--scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--microsoft-graph-remote-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--file**|object|file|file|file|
|**--microsoft-graph-file-system-info-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--folder**|object|folder|folder|folder|
|**--microsoft-graph-remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--microsoft-graph-image**|object|image|microsoft_graph_image|image|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--microsoft-graph-remote-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--package**|object|package|package|package|
|**--parent-reference**|object|itemReference|parent_reference|parentReference|
|**--shared**|object|shared|shared|shared|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--integer-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--special-folder**|object|specialFolder|special_folder|specialFolder|
|**--microsoft-graph-video**|object|video|microsoft_graph_video|video|
|**--microsoft-graph-remote-item-web-dav-url-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--microsoft-graph-remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--view**|object|folderView|view|view|
|**--hashes**|object|hashes|hashes|hashes|
|**--mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--state**|string|Represents the state of the deleted item.|state|state|
|**--album**|object|album|album|album|
|**--integer-child-count**|integer||integer_child_count|childCount|

#### <a name="teams.channelsUpdateMembers">Command `az teams team-channel update-member`</a>

##### <a name="Parametersteams.channelsUpdateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teams.channelsUpdateMessages">Command `az teams team-channel update-message`</a>

##### <a name="Parametersteams.channelsUpdateMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--chat-id**|string||chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.channelsUpdateTabs">Command `az teams team-channel update-tab`</a>

##### <a name="Parametersteams.channelsUpdateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--message-id**|string||message_id|messageId|
|**--sort-order-index**|string||sort_order_index|sortOrderIndex|
|**--teams-app-id**|string||teams_app_id|teamsAppId|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### group `az teams team-channel-member`
#### <a name="teams.channels.membersadd">Command `az teams team-channel-member add`</a>

##### <a name="Parametersteams.channels.membersadd">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--values**|array||values|values|

### group `az teams team-channel-message`
#### <a name="teams.channels.messagesCreateHostedContents">Command `az teams team-channel-message create-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesCreateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--content-bytes**|byte-array||content_bytes|contentBytes|
|**--content-type**|string||content_type|contentType|

#### <a name="teams.channels.messagesCreateReplies">Command `az teams team-channel-message create-reply`</a>

##### <a name="Parametersteams.channels.messagesCreateReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--chat-id**|string||chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.channels.messagesDeleteHostedContents">Command `az teams team-channel-message delete-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesDeleteHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channels.messagesDeleteReplies">Command `az teams team-channel-message delete-reply`</a>

##### <a name="Parametersteams.channels.messagesDeleteReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channels.messagesdelta">Command `az teams team-channel-message delta`</a>

##### <a name="Parametersteams.channels.messagesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|

#### <a name="teams.channels.messagesListHostedContents">Command `az teams team-channel-message list-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesListHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channels.messagesListReplies">Command `az teams team-channel-message list-reply`</a>

##### <a name="Parametersteams.channels.messagesListReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channels.messagesSetHostedContentsContent">Command `az teams team-channel-message set-hosted-content-content`</a>

##### <a name="Parametersteams.channels.messagesSetHostedContentsContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--data**|binary|New media content.|data|data|

#### <a name="teams.channels.messagesGetHostedContents">Command `az teams team-channel-message show-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesGetHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channels.messagesGetHostedContentsContent">Command `az teams team-channel-message show-hosted-content-content`</a>

##### <a name="Parametersteams.channels.messagesGetHostedContentsContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|

#### <a name="teams.channels.messagesGetReplies">Command `az teams team-channel-message show-reply`</a>

##### <a name="Parametersteams.channels.messagesGetReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channels.messagesUpdateHostedContents">Command `az teams team-channel-message update-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesUpdateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--id**|string|Read-only.|id|id|
|**--content-bytes**|byte-array||content_bytes|contentBytes|
|**--content-type**|string||content_type|contentType|

#### <a name="teams.channels.messagesUpdateReplies">Command `az teams team-channel-message update-reply`</a>

##### <a name="Parametersteams.channels.messagesUpdateReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--chat-id**|string||chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

### group `az teams team-channel-message-reply`
#### <a name="teams.channels.messages.repliesdelta">Command `az teams team-channel-message-reply delta`</a>

##### <a name="Parametersteams.channels.messages.repliesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|

### group `az teams team-channel-tab`
#### <a name="teams.channels.tabsDeleteRefTeamsApp">Command `az teams team-channel-tab delete-ref-team-app`</a>

##### <a name="Parametersteams.channels.tabsDeleteRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channels.tabsSetRefTeamsApp">Command `az teams team-channel-tab set-ref-team-app`</a>

##### <a name="Parametersteams.channels.tabsSetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teams.channels.tabsGetRefTeamsApp">Command `az teams team-channel-tab show-ref-team-app`</a>

##### <a name="Parametersteams.channels.tabsGetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|

#### <a name="teams.channels.tabsGetTeamsApp">Command `az teams team-channel-tab show-team-app`</a>

##### <a name="Parametersteams.channels.tabsGetTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az teams team-installed-app`
#### <a name="teams.installedAppsDeleteRefTeamsApp">Command `az teams team-installed-app delete-ref-team-app`</a>

##### <a name="Parametersteams.installedAppsDeleteRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.installedAppsDeleteRefTeamsAppDefinition">Command `az teams team-installed-app delete-ref-team-app-definition`</a>

##### <a name="Parametersteams.installedAppsDeleteRefTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.installedAppsSetRefTeamsApp">Command `az teams team-installed-app set-ref-team-app`</a>

##### <a name="Parametersteams.installedAppsSetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teams.installedAppsSetRefTeamsAppDefinition">Command `az teams team-installed-app set-ref-team-app-definition`</a>

##### <a name="Parametersteams.installedAppsSetRefTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teams.installedAppsGetRefTeamsApp">Command `az teams team-installed-app show-ref-team-app`</a>

##### <a name="Parametersteams.installedAppsGetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

#### <a name="teams.installedAppsGetRefTeamsAppDefinition">Command `az teams team-installed-app show-ref-team-app-definition`</a>

##### <a name="Parametersteams.installedAppsGetRefTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

#### <a name="teams.installedAppsGetTeamsApp">Command `az teams team-installed-app show-team-app`</a>

##### <a name="Parametersteams.installedAppsGetTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.installedAppsGetTeamsAppDefinition">Command `az teams team-installed-app show-team-app-definition`</a>

##### <a name="Parametersteams.installedAppsGetTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.installedAppsupgrade">Command `az teams team-installed-app upgrade`</a>

##### <a name="Parametersteams.installedAppsupgrade">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

### group `az teams team-member`
#### <a name="teams.membersadd">Command `az teams team-member add`</a>

##### <a name="Parametersteams.membersadd">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--values**|array||values|values|

### group `az teams team-primary-channel`
#### <a name="teams.primaryChannelcompleteMigration">Command `az teams team-primary-channel complete-migration`</a>

##### <a name="Parametersteams.primaryChannelcompleteMigration">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teams.primaryChannelCreateMembers">Command `az teams team-primary-channel create-member`</a>

##### <a name="Parametersteams.primaryChannelCreateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teams.primaryChannelCreateMessages">Command `az teams team-primary-channel create-message`</a>

##### <a name="Parametersteams.primaryChannelCreateMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--chat-id**|string||chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.primaryChannelCreateTabs">Command `az teams team-primary-channel create-tab`</a>

##### <a name="Parametersteams.primaryChannelCreateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--message-id**|string||message_id|messageId|
|**--sort-order-index**|string||sort_order_index|sortOrderIndex|
|**--teams-app-id**|string||teams_app_id|teamsAppId|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="teams.primaryChannelDeleteFilesFolder">Command `az teams team-primary-channel delete-file-folder`</a>

##### <a name="Parametersteams.primaryChannelDeleteFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannelDeleteMembers">Command `az teams team-primary-channel delete-member`</a>

##### <a name="Parametersteams.primaryChannelDeleteMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannelDeleteMessages">Command `az teams team-primary-channel delete-message`</a>

##### <a name="Parametersteams.primaryChannelDeleteMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannelDeleteTabs">Command `az teams team-primary-channel delete-tab`</a>

##### <a name="Parametersteams.primaryChannelDeleteTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannelListMembers">Command `az teams team-primary-channel list-member`</a>

##### <a name="Parametersteams.primaryChannelListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelListMessages">Command `az teams team-primary-channel list-message`</a>

##### <a name="Parametersteams.primaryChannelListMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelListTabs">Command `az teams team-primary-channel list-tab`</a>

##### <a name="Parametersteams.primaryChannelListTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelSetFilesFolderContent">Command `az teams team-primary-channel set-file-folder-content`</a>

##### <a name="Parametersteams.primaryChannelSetFilesFolderContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--data**|binary|New media content.|data|data|

#### <a name="teams.primaryChannelGetFilesFolder">Command `az teams team-primary-channel show-file-folder`</a>

##### <a name="Parametersteams.primaryChannelGetFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelGetFilesFolderContent">Command `az teams team-primary-channel show-file-folder-content`</a>

##### <a name="Parametersteams.primaryChannelGetFilesFolderContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teams.primaryChannelGetMembers">Command `az teams team-primary-channel show-member`</a>

##### <a name="Parametersteams.primaryChannelGetMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelGetMessages">Command `az teams team-primary-channel show-message`</a>

##### <a name="Parametersteams.primaryChannelGetMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelGetTabs">Command `az teams team-primary-channel show-tab`</a>

##### <a name="Parametersteams.primaryChannelGetTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelUpdateFilesFolder">Command `az teams team-primary-channel update-file-folder`</a>

##### <a name="Parametersteams.primaryChannelUpdateFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--activities**|array|The list of recent activities that took place on this item.|activities|activities|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--list-item**|object|listItem|list_item|listItem|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--all-time**|object|itemActivityStat|all_time|allTime|
|**--item-activity-stats**|array||item_activity_stats|itemActivityStats|
|**--last-seven-days**|object|itemActivityStat|last_seven_days|lastSevenDays|
|**--id1**|string|Read-only.|id1|id|
|**--microsoft-graph-workbook-application**|object|workbookApplication|microsoft_graph_workbook_application|application|
|**--comments**|array||comments|comments|
|**--functions**|object|workbookFunctions|functions|functions|
|**--names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--microsoft-graph-special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--owner**|object|identitySet|owner|owner|
|**--scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--microsoft-graph-remote-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--file**|object|file|file|file|
|**--microsoft-graph-file-system-info-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--folder**|object|folder|folder|folder|
|**--microsoft-graph-remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--microsoft-graph-image**|object|image|microsoft_graph_image|image|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--microsoft-graph-remote-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--package**|object|package|package|package|
|**--parent-reference**|object|itemReference|parent_reference|parentReference|
|**--shared**|object|shared|shared|shared|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--integer-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--special-folder**|object|specialFolder|special_folder|specialFolder|
|**--microsoft-graph-video**|object|video|microsoft_graph_video|video|
|**--microsoft-graph-remote-item-web-dav-url-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--microsoft-graph-remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--view**|object|folderView|view|view|
|**--hashes**|object|hashes|hashes|hashes|
|**--mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--state**|string|Represents the state of the deleted item.|state|state|
|**--album**|object|album|album|album|
|**--integer-child-count**|integer||integer_child_count|childCount|

#### <a name="teams.primaryChannelUpdateMembers">Command `az teams team-primary-channel update-member`</a>

##### <a name="Parametersteams.primaryChannelUpdateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teams.primaryChannelUpdateMessages">Command `az teams team-primary-channel update-message`</a>

##### <a name="Parametersteams.primaryChannelUpdateMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--chat-id**|string||chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.primaryChannelUpdateTabs">Command `az teams team-primary-channel update-tab`</a>

##### <a name="Parametersteams.primaryChannelUpdateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--message-id**|string||message_id|messageId|
|**--sort-order-index**|string||sort_order_index|sortOrderIndex|
|**--teams-app-id**|string||teams_app_id|teamsAppId|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### group `az teams team-primary-channel-member`
#### <a name="teams.primaryChannel.membersadd">Command `az teams team-primary-channel-member add`</a>

##### <a name="Parametersteams.primaryChannel.membersadd">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--values**|array||values|values|

### group `az teams team-primary-channel-message`
#### <a name="teams.primaryChannel.messagesCreateHostedContents">Command `az teams team-primary-channel-message create-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesCreateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--content-bytes**|byte-array||content_bytes|contentBytes|
|**--content-type**|string||content_type|contentType|

#### <a name="teams.primaryChannel.messagesCreateReplies">Command `az teams team-primary-channel-message create-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesCreateReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--chat-id**|string||chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.primaryChannel.messagesDeleteHostedContents">Command `az teams team-primary-channel-message delete-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesDeleteHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannel.messagesDeleteReplies">Command `az teams team-primary-channel-message delete-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesDeleteReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannel.messagesdelta">Command `az teams team-primary-channel-message delta`</a>

##### <a name="Parametersteams.primaryChannel.messagesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teams.primaryChannel.messagesListHostedContents">Command `az teams team-primary-channel-message list-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesListHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannel.messagesListReplies">Command `az teams team-primary-channel-message list-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesListReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannel.messagesSetHostedContentsContent">Command `az teams team-primary-channel-message set-hosted-content-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesSetHostedContentsContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--data**|binary|New media content.|data|data|

#### <a name="teams.primaryChannel.messagesGetHostedContents">Command `az teams team-primary-channel-message show-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesGetHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannel.messagesGetHostedContentsContent">Command `az teams team-primary-channel-message show-hosted-content-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesGetHostedContentsContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|

#### <a name="teams.primaryChannel.messagesGetReplies">Command `az teams team-primary-channel-message show-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesGetReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannel.messagesUpdateHostedContents">Command `az teams team-primary-channel-message update-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesUpdateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--id**|string|Read-only.|id|id|
|**--content-bytes**|byte-array||content_bytes|contentBytes|
|**--content-type**|string||content_type|contentType|

#### <a name="teams.primaryChannel.messagesUpdateReplies">Command `az teams team-primary-channel-message update-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesUpdateReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--channel-identity**|object|channelIdentity|channel_identity|channelIdentity|
|**--chat-id**|string||chat_id|chatId|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string|Justification text provided by the sender of the message when overriding a policy violation.|justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

### group `az teams team-primary-channel-message-reply`
#### <a name="teams.primaryChannel.messages.repliesdelta">Command `az teams team-primary-channel-message-reply delta`</a>

##### <a name="Parametersteams.primaryChannel.messages.repliesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|

### group `az teams team-primary-channel-tab`
#### <a name="teams.primaryChannel.tabsDeleteRefTeamsApp">Command `az teams team-primary-channel-tab delete-ref-team-app`</a>

##### <a name="Parametersteams.primaryChannel.tabsDeleteRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannel.tabsSetRefTeamsApp">Command `az teams team-primary-channel-tab set-ref-team-app`</a>

##### <a name="Parametersteams.primaryChannel.tabsSetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teams.primaryChannel.tabsGetRefTeamsApp">Command `az teams team-primary-channel-tab show-ref-team-app`</a>

##### <a name="Parametersteams.primaryChannel.tabsGetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|

#### <a name="teams.primaryChannel.tabsGetTeamsApp">Command `az teams team-primary-channel-tab show-team-app`</a>

##### <a name="Parametersteams.primaryChannel.tabsGetTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az teams team-schedule`
#### <a name="teams.scheduleCreateOfferShiftRequests">Command `az teams team-schedule create-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleCreateOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--recipient-action-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|recipient_action_date_time|recipientActionDateTime|
|**--recipient-action-message**|string|Custom message sent by recipient of the offer shift request.|recipient_action_message|recipientActionMessage|
|**--recipient-user-id**|string|User ID of the recipient of the offer shift request.|recipient_user_id|recipientUserId|
|**--sender-shift-id**|string|User ID of the sender of the offer shift request.|sender_shift_id|senderShiftId|

#### <a name="teams.scheduleCreateOpenShifts">Command `az teams team-schedule create-open-shift`</a>

##### <a name="Parametersteams.scheduleCreateOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--draft-open-shift**|object|openShiftItem|draft_open_shift|draftOpenShift|
|**--is-staged-for-deletion**|boolean||is_staged_for_deletion|isStagedForDeletion|
|**--scheduling-group-id**|string|ID for the scheduling group that the open shift belongs to.|scheduling_group_id|schedulingGroupId|
|**--shared-open-shift**|object|openShiftItem|shared_open_shift|sharedOpenShift|

#### <a name="teams.scheduleCreateOpenShiftChangeRequests">Command `az teams team-schedule create-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleCreateOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--open-shift-id**|string|ID for the open shift.|open_shift_id|openShiftId|

#### <a name="teams.scheduleCreateSchedulingGroups">Command `az teams team-schedule create-scheduling-group`</a>

##### <a name="Parametersteams.scheduleCreateSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string|The display name for the schedulingGroup. Required.|display_name|displayName|
|**--is-active**|boolean|Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.|is_active|isActive|
|**--user-ids**|array|The list of user IDs that are a member of the schedulingGroup. Required.|user_ids|userIds|

#### <a name="teams.scheduleCreateShifts">Command `az teams team-schedule create-shift`</a>

##### <a name="Parametersteams.scheduleCreateShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-staged-for-deletion**|boolean||is_staged_for_deletion|isStagedForDeletion|
|**--scheduling-group-id**|string|ID of the scheduling group the shift is part of. Required.|scheduling_group_id|schedulingGroupId|
|**--user-id**|string|ID of the user assigned to the shift. Required.|user_id|userId|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--theme**|choice||theme|theme|
|**--activities**|array|An incremental part of a shift which can cover details of when and where an employee is during their shift. For example, an assignment or a scheduled break or lunch. Required.|activities|activities|
|**--display-name**|string|The shift label of the shiftItem.|display_name|displayName|
|**--notes**|string|The shift notes for the shiftItem.|notes|notes|
|**--microsoft-graph-schedule-entity-end-date-time-end-date-time**|date-time||microsoft_graph_schedule_entity_end_date_time_end_date_time|endDateTime|
|**--microsoft-graph-schedule-entity-start-date-time-start-date-time**|date-time||microsoft_graph_schedule_entity_start_date_time_start_date_time|startDateTime|
|**--microsoft-graph-schedule-entity-theme**|choice||microsoft_graph_schedule_entity_theme|theme|
|**--microsoft-graph-shift-item-activities**|array|An incremental part of a shift which can cover details of when and where an employee is during their shift. For example, an assignment or a scheduled break or lunch. Required.|microsoft_graph_shift_item_activities|activities|
|**--microsoft-graph-shift-item-display-name**|string|The shift label of the shiftItem.|microsoft_graph_shift_item_display_name|displayName|
|**--microsoft-graph-shift-item-notes**|string|The shift notes for the shiftItem.|microsoft_graph_shift_item_notes|notes|

#### <a name="teams.scheduleCreateSwapShiftsChangeRequests">Command `az teams team-schedule create-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleCreateSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--recipient-action-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|recipient_action_date_time|recipientActionDateTime|
|**--recipient-action-message**|string|Custom message sent by recipient of the offer shift request.|recipient_action_message|recipientActionMessage|
|**--recipient-user-id**|string|User ID of the recipient of the offer shift request.|recipient_user_id|recipientUserId|
|**--sender-shift-id**|string|User ID of the sender of the offer shift request.|sender_shift_id|senderShiftId|
|**--recipient-shift-id**|string|ShiftId for the recipient user with whom the request is to swap.|recipient_shift_id|recipientShiftId|

#### <a name="teams.scheduleCreateTimeCards">Command `az teams team-schedule create-time-card`</a>

##### <a name="Parametersteams.scheduleCreateTimeCards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--breaks**|array||breaks|breaks|
|**--confirmed-by**|choice||confirmed_by|confirmedBy|
|**--notes**|object|itemBody|notes|notes|
|**--state**|choice||state|state|
|**--user-id**|string||user_id|userId|
|**--microsoft-graph-time-card-entry-breaks**|array||microsoft_graph_time_card_entry_breaks|breaks|
|**--clock-in-event**|object|timeCardEvent|clock_in_event|clockInEvent|
|**--clock-out-event**|object|timeCardEvent|clock_out_event|clockOutEvent|
|**--at-approved-location**|boolean||at_approved_location|atApprovedLocation|
|**--date-time**|date-time||date_time|dateTime|
|**--microsoft-graph-item-body-notes**|object|itemBody|microsoft_graph_item_body_notes|notes|
|**--boolean-at-approved-location**|boolean||boolean_at_approved_location|atApprovedLocation|
|**--microsoft-graph-time-card-event-date-time**|date-time||microsoft_graph_time_card_event_date_time|dateTime|
|**--notes1**|object|itemBody|notes1|notes|

#### <a name="teams.scheduleCreateTimesOff">Command `az teams team-schedule create-time-off`</a>

##### <a name="Parametersteams.scheduleCreateTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--draft-time-off**|object|timeOffItem|draft_time_off|draftTimeOff|
|**--is-staged-for-deletion**|boolean||is_staged_for_deletion|isStagedForDeletion|
|**--shared-time-off**|object|timeOffItem|shared_time_off|sharedTimeOff|
|**--user-id**|string|ID of the user assigned to the timeOff. Required.|user_id|userId|

#### <a name="teams.scheduleCreateTimeOffReasons">Command `az teams team-schedule create-time-off-reason`</a>

##### <a name="Parametersteams.scheduleCreateTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string|The name of the timeOffReason. Required.|display_name|displayName|
|**--icon-type**|choice||icon_type|iconType|
|**--is-active**|boolean|Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.|is_active|isActive|

#### <a name="teams.scheduleCreateTimeOffRequests">Command `az teams team-schedule create-time-off-request`</a>

##### <a name="Parametersteams.scheduleCreateTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--end-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--start-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--time-off-reason-id**|string|The reason for the time off.|time_off_reason_id|timeOffReasonId|

#### <a name="teams.scheduleDeleteOfferShiftRequests">Command `az teams team-schedule delete-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleDeleteOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--offer-shift-request-id**|string|key: id of offerShiftRequest|offer_shift_request_id|offerShiftRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteOpenShifts">Command `az teams team-schedule delete-open-shift`</a>

##### <a name="Parametersteams.scheduleDeleteOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-id**|string|key: id of openShift|open_shift_id|openShift-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteOpenShiftChangeRequests">Command `az teams team-schedule delete-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleDeleteOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-change-request-id**|string|key: id of openShiftChangeRequest|open_shift_change_request_id|openShiftChangeRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteSchedulingGroups">Command `az teams team-schedule delete-scheduling-group`</a>

##### <a name="Parametersteams.scheduleDeleteSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--scheduling-group-id**|string|key: id of schedulingGroup|scheduling_group_id|schedulingGroup-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteShifts">Command `az teams team-schedule delete-shift`</a>

##### <a name="Parametersteams.scheduleDeleteShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--shift-id**|string|key: id of shift|shift_id|shift-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteSwapShiftsChangeRequests">Command `az teams team-schedule delete-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleDeleteSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--swap-shifts-change-request-id**|string|key: id of swapShiftsChangeRequest|swap_shifts_change_request_id|swapShiftsChangeRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteTimeCards">Command `az teams team-schedule delete-time-card`</a>

##### <a name="Parametersteams.scheduleDeleteTimeCards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-card-id**|string|key: id of timeCard|time_card_id|timeCard-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteTimesOff">Command `az teams team-schedule delete-time-off`</a>

##### <a name="Parametersteams.scheduleDeleteTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-id**|string|key: id of timeOff|time_off_id|timeOff-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteTimeOffReasons">Command `az teams team-schedule delete-time-off-reason`</a>

##### <a name="Parametersteams.scheduleDeleteTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-reason-id**|string|key: id of timeOffReason|time_off_reason_id|timeOffReason-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteTimeOffRequests">Command `az teams team-schedule delete-time-off-request`</a>

##### <a name="Parametersteams.scheduleDeleteTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-request-id**|string|key: id of timeOffRequest|time_off_request_id|timeOffRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleListOfferShiftRequests">Command `az teams team-schedule list-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleListOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListOpenShifts">Command `az teams team-schedule list-open-shift`</a>

##### <a name="Parametersteams.scheduleListOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListOpenShiftChangeRequests">Command `az teams team-schedule list-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleListOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListSchedulingGroups">Command `az teams team-schedule list-scheduling-group`</a>

##### <a name="Parametersteams.scheduleListSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListShifts">Command `az teams team-schedule list-shift`</a>

##### <a name="Parametersteams.scheduleListShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListSwapShiftsChangeRequests">Command `az teams team-schedule list-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleListSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListTimeCards">Command `az teams team-schedule list-time-card`</a>

##### <a name="Parametersteams.scheduleListTimeCards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListTimesOff">Command `az teams team-schedule list-time-off`</a>

##### <a name="Parametersteams.scheduleListTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListTimeOffReasons">Command `az teams team-schedule list-time-off-reason`</a>

##### <a name="Parametersteams.scheduleListTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListTimeOffRequests">Command `az teams team-schedule list-time-off-request`</a>

##### <a name="Parametersteams.scheduleListTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleshare">Command `az teams team-schedule share`</a>

##### <a name="Parametersteams.scheduleshare">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--notify-team**|boolean||notify_team|notifyTeam|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|

#### <a name="teams.scheduleGetOfferShiftRequests">Command `az teams team-schedule show-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleGetOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--offer-shift-request-id**|string|key: id of offerShiftRequest|offer_shift_request_id|offerShiftRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetOpenShifts">Command `az teams team-schedule show-open-shift`</a>

##### <a name="Parametersteams.scheduleGetOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-id**|string|key: id of openShift|open_shift_id|openShift-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetOpenShiftChangeRequests">Command `az teams team-schedule show-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleGetOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-change-request-id**|string|key: id of openShiftChangeRequest|open_shift_change_request_id|openShiftChangeRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetSchedulingGroups">Command `az teams team-schedule show-scheduling-group`</a>

##### <a name="Parametersteams.scheduleGetSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--scheduling-group-id**|string|key: id of schedulingGroup|scheduling_group_id|schedulingGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetShifts">Command `az teams team-schedule show-shift`</a>

##### <a name="Parametersteams.scheduleGetShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--shift-id**|string|key: id of shift|shift_id|shift-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetSwapShiftsChangeRequests">Command `az teams team-schedule show-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleGetSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--swap-shifts-change-request-id**|string|key: id of swapShiftsChangeRequest|swap_shifts_change_request_id|swapShiftsChangeRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetTimeCards">Command `az teams team-schedule show-time-card`</a>

##### <a name="Parametersteams.scheduleGetTimeCards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-card-id**|string|key: id of timeCard|time_card_id|timeCard-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetTimesOff">Command `az teams team-schedule show-time-off`</a>

##### <a name="Parametersteams.scheduleGetTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-id**|string|key: id of timeOff|time_off_id|timeOff-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetTimeOffReasons">Command `az teams team-schedule show-time-off-reason`</a>

##### <a name="Parametersteams.scheduleGetTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-reason-id**|string|key: id of timeOffReason|time_off_reason_id|timeOffReason-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetTimeOffRequests">Command `az teams team-schedule show-time-off-request`</a>

##### <a name="Parametersteams.scheduleGetTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-request-id**|string|key: id of timeOffRequest|time_off_request_id|timeOffRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleUpdateOfferShiftRequests">Command `az teams team-schedule update-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleUpdateOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--offer-shift-request-id**|string|key: id of offerShiftRequest|offer_shift_request_id|offerShiftRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--recipient-action-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|recipient_action_date_time|recipientActionDateTime|
|**--recipient-action-message**|string|Custom message sent by recipient of the offer shift request.|recipient_action_message|recipientActionMessage|
|**--recipient-user-id**|string|User ID of the recipient of the offer shift request.|recipient_user_id|recipientUserId|
|**--sender-shift-id**|string|User ID of the sender of the offer shift request.|sender_shift_id|senderShiftId|

#### <a name="teams.scheduleUpdateOpenShifts">Command `az teams team-schedule update-open-shift`</a>

##### <a name="Parametersteams.scheduleUpdateOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-id**|string|key: id of openShift|open_shift_id|openShift-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--draft-open-shift**|object|openShiftItem|draft_open_shift|draftOpenShift|
|**--is-staged-for-deletion**|boolean||is_staged_for_deletion|isStagedForDeletion|
|**--scheduling-group-id**|string|ID for the scheduling group that the open shift belongs to.|scheduling_group_id|schedulingGroupId|
|**--shared-open-shift**|object|openShiftItem|shared_open_shift|sharedOpenShift|

#### <a name="teams.scheduleUpdateOpenShiftChangeRequests">Command `az teams team-schedule update-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleUpdateOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-change-request-id**|string|key: id of openShiftChangeRequest|open_shift_change_request_id|openShiftChangeRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--open-shift-id**|string|ID for the open shift.|open_shift_id|openShiftId|

#### <a name="teams.scheduleUpdateSchedulingGroups">Command `az teams team-schedule update-scheduling-group`</a>

##### <a name="Parametersteams.scheduleUpdateSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--scheduling-group-id**|string|key: id of schedulingGroup|scheduling_group_id|schedulingGroup-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string|The display name for the schedulingGroup. Required.|display_name|displayName|
|**--is-active**|boolean|Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.|is_active|isActive|
|**--user-ids**|array|The list of user IDs that are a member of the schedulingGroup. Required.|user_ids|userIds|

#### <a name="teams.scheduleUpdateShifts">Command `az teams team-schedule update-shift`</a>

##### <a name="Parametersteams.scheduleUpdateShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--shift-id**|string|key: id of shift|shift_id|shift-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--is-staged-for-deletion**|boolean||is_staged_for_deletion|isStagedForDeletion|
|**--scheduling-group-id**|string|ID of the scheduling group the shift is part of. Required.|scheduling_group_id|schedulingGroupId|
|**--user-id**|string|ID of the user assigned to the shift. Required.|user_id|userId|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--theme**|choice||theme|theme|
|**--activities**|array|An incremental part of a shift which can cover details of when and where an employee is during their shift. For example, an assignment or a scheduled break or lunch. Required.|activities|activities|
|**--display-name**|string|The shift label of the shiftItem.|display_name|displayName|
|**--notes**|string|The shift notes for the shiftItem.|notes|notes|
|**--microsoft-graph-schedule-entity-end-date-time-end-date-time**|date-time||microsoft_graph_schedule_entity_end_date_time_end_date_time|endDateTime|
|**--microsoft-graph-schedule-entity-start-date-time-start-date-time**|date-time||microsoft_graph_schedule_entity_start_date_time_start_date_time|startDateTime|
|**--microsoft-graph-schedule-entity-theme**|choice||microsoft_graph_schedule_entity_theme|theme|
|**--microsoft-graph-shift-item-activities**|array|An incremental part of a shift which can cover details of when and where an employee is during their shift. For example, an assignment or a scheduled break or lunch. Required.|microsoft_graph_shift_item_activities|activities|
|**--microsoft-graph-shift-item-display-name**|string|The shift label of the shiftItem.|microsoft_graph_shift_item_display_name|displayName|
|**--microsoft-graph-shift-item-notes**|string|The shift notes for the shiftItem.|microsoft_graph_shift_item_notes|notes|

#### <a name="teams.scheduleUpdateSwapShiftsChangeRequests">Command `az teams team-schedule update-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleUpdateSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--swap-shifts-change-request-id**|string|key: id of swapShiftsChangeRequest|swap_shifts_change_request_id|swapShiftsChangeRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--recipient-action-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|recipient_action_date_time|recipientActionDateTime|
|**--recipient-action-message**|string|Custom message sent by recipient of the offer shift request.|recipient_action_message|recipientActionMessage|
|**--recipient-user-id**|string|User ID of the recipient of the offer shift request.|recipient_user_id|recipientUserId|
|**--sender-shift-id**|string|User ID of the sender of the offer shift request.|sender_shift_id|senderShiftId|
|**--recipient-shift-id**|string|ShiftId for the recipient user with whom the request is to swap.|recipient_shift_id|recipientShiftId|

#### <a name="teams.scheduleUpdateTimeCards">Command `az teams team-schedule update-time-card`</a>

##### <a name="Parametersteams.scheduleUpdateTimeCards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-card-id**|string|key: id of timeCard|time_card_id|timeCard-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--breaks**|array||breaks|breaks|
|**--confirmed-by**|choice||confirmed_by|confirmedBy|
|**--notes**|object|itemBody|notes|notes|
|**--state**|choice||state|state|
|**--user-id**|string||user_id|userId|
|**--microsoft-graph-time-card-entry-breaks**|array||microsoft_graph_time_card_entry_breaks|breaks|
|**--clock-in-event**|object|timeCardEvent|clock_in_event|clockInEvent|
|**--clock-out-event**|object|timeCardEvent|clock_out_event|clockOutEvent|
|**--at-approved-location**|boolean||at_approved_location|atApprovedLocation|
|**--date-time**|date-time||date_time|dateTime|
|**--microsoft-graph-item-body-notes**|object|itemBody|microsoft_graph_item_body_notes|notes|
|**--boolean-at-approved-location**|boolean||boolean_at_approved_location|atApprovedLocation|
|**--microsoft-graph-time-card-event-date-time**|date-time||microsoft_graph_time_card_event_date_time|dateTime|
|**--notes1**|object|itemBody|notes1|notes|

#### <a name="teams.scheduleUpdateTimesOff">Command `az teams team-schedule update-time-off`</a>

##### <a name="Parametersteams.scheduleUpdateTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-id**|string|key: id of timeOff|time_off_id|timeOff-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--draft-time-off**|object|timeOffItem|draft_time_off|draftTimeOff|
|**--is-staged-for-deletion**|boolean||is_staged_for_deletion|isStagedForDeletion|
|**--shared-time-off**|object|timeOffItem|shared_time_off|sharedTimeOff|
|**--user-id**|string|ID of the user assigned to the timeOff. Required.|user_id|userId|

#### <a name="teams.scheduleUpdateTimeOffReasons">Command `az teams team-schedule update-time-off-reason`</a>

##### <a name="Parametersteams.scheduleUpdateTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-reason-id**|string|key: id of timeOffReason|time_off_reason_id|timeOffReason-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string|The name of the timeOffReason. Required.|display_name|displayName|
|**--icon-type**|choice||icon_type|iconType|
|**--is-active**|boolean|Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.|is_active|isActive|

#### <a name="teams.scheduleUpdateTimeOffRequests">Command `az teams team-schedule update-time-off-request`</a>

##### <a name="Parametersteams.scheduleUpdateTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-request-id**|string|key: id of timeOffRequest|time_off_request_id|timeOffRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--end-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--start-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--time-off-reason-id**|string|The reason for the time off.|time_off_reason_id|timeOffReasonId|

### group `az teams team-schedule-time-card`
#### <a name="teams.schedule.timeCardsclockIn">Command `az teams team-schedule-time-card clock-in`</a>

##### <a name="Parametersteams.schedule.timeCardsclockIn">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--at-approved-location**|boolean||at_approved_location|atApprovedLocation|
|**--on-behalf-of-user-id**|string||on_behalf_of_user_id|onBehalfOfUserId|
|**--notes**|object|itemBody|notes|notes|

#### <a name="teams.schedule.timeCardsclockOut">Command `az teams team-schedule-time-card clock-out`</a>

##### <a name="Parametersteams.schedule.timeCardsclockOut">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-card-id**|string|key: id of timeCard|time_card_id|timeCard-id|
|**--at-approved-location**|boolean||at_approved_location|atApprovedLocation|
|**--notes**|object|itemBody|notes|notes|

#### <a name="teams.schedule.timeCardsconfirm">Command `az teams team-schedule-time-card confirm`</a>

##### <a name="Parametersteams.schedule.timeCardsconfirm">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-card-id**|string|key: id of timeCard|time_card_id|timeCard-id|

#### <a name="teams.schedule.timeCardsendBreak">Command `az teams team-schedule-time-card end-break`</a>

##### <a name="Parametersteams.schedule.timeCardsendBreak">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-card-id**|string|key: id of timeCard|time_card_id|timeCard-id|
|**--at-approved-location**|boolean||at_approved_location|atApprovedLocation|
|**--notes**|object|itemBody|notes|notes|

#### <a name="teams.schedule.timeCardsstartBreak">Command `az teams team-schedule-time-card start-break`</a>

##### <a name="Parametersteams.schedule.timeCardsstartBreak">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-card-id**|string|key: id of timeCard|time_card_id|timeCard-id|
|**--at-approved-location**|boolean||at_approved_location|atApprovedLocation|
|**--notes**|object|itemBody|notes|notes|

### group `az teams teamwork`
#### <a name="teamworkCreateWorkforceIntegrations">Command `az teams teamwork create-workforce-integration`</a>

##### <a name="ParametersteamworkCreateWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--api-version**|integer|API version for the call back URL. Start with 1.|api_version|apiVersion|
|**--display-name**|string|Name of the workforce integration.|display_name|displayName|
|**--eligibility-filtering-enabled-entities**|choice||eligibility_filtering_enabled_entities|eligibilityFilteringEnabledEntities|
|**--encryption**|object|workforceIntegrationEncryption|encryption|encryption|
|**--is-active**|boolean|Indicates whether this workforce integration is currently active and available.|is_active|isActive|
|**--supported-entities**|choice||supported_entities|supportedEntities|
|**--supports**|choice||supports|supports|
|**--url**|string|Workforce Integration URL for callbacks from the Shifts service.|url|url|

#### <a name="teamworkDeleteWorkforceIntegrations">Command `az teams teamwork delete-workforce-integration`</a>

##### <a name="ParametersteamworkDeleteWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--workforce-integration-id**|string|key: id of workforceIntegration|workforce_integration_id|workforceIntegration-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamworkListWorkforceIntegrations">Command `az teams teamwork list-workforce-integration`</a>

##### <a name="ParametersteamworkListWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamworkGetWorkforceIntegrations">Command `az teams teamwork show-workforce-integration`</a>

##### <a name="ParametersteamworkGetWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--workforce-integration-id**|string|key: id of workforceIntegration|workforce_integration_id|workforceIntegration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamworkUpdateWorkforceIntegrations">Command `az teams teamwork update-workforce-integration`</a>

##### <a name="ParametersteamworkUpdateWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--workforce-integration-id**|string|key: id of workforceIntegration|workforce_integration_id|workforceIntegration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--api-version**|integer|API version for the call back URL. Start with 1.|api_version|apiVersion|
|**--display-name**|string|Name of the workforce integration.|display_name|displayName|
|**--eligibility-filtering-enabled-entities**|choice||eligibility_filtering_enabled_entities|eligibilityFilteringEnabledEntities|
|**--encryption**|object|workforceIntegrationEncryption|encryption|encryption|
|**--is-active**|boolean|Indicates whether this workforce integration is currently active and available.|is_active|isActive|
|**--supported-entities**|choice||supported_entities|supportedEntities|
|**--supports**|choice||supports|supports|
|**--url**|string|Workforce Integration URL for callbacks from the Shifts service.|url|url|

### group `az teams teamwork-teamwork`
#### <a name="teamwork.teamworkGetTeamwork">Command `az teams teamwork-teamwork show-teamwork`</a>

##### <a name="Parametersteamwork.teamworkGetTeamwork">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamwork.teamworkUpdateTeamwork">Command `az teams teamwork-teamwork update-teamwork`</a>

##### <a name="Parametersteamwork.teamworkUpdateTeamwork">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--workforce-integrations**|array||workforce_integrations|workforceIntegrations|

### group `az teams user`
#### <a name="usersCreateChats">Command `az teams user create-chat`</a>

##### <a name="ParametersusersCreateChats">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--topic**|string||topic|topic|
|**--installed-apps**|array||installed_apps|installedApps|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--tabs**|array||tabs|tabs|

#### <a name="usersCreateJoinedTeams">Command `az teams user create-joined-team`</a>

##### <a name="ParametersusersCreateJoinedTeams">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--is-membership-limited-to-owners**|boolean||is_membership_limited_to_owners|isMembershipLimitedToOwners|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--owners**|array||owners|owners|
|**--photo**|object|profilePhoto|photo|photo|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--provision-status**|choice||provision_status|provisionStatus|
|**--provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--open-shifts**|array||open_shifts|openShifts|
|**--scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--time-cards**|array||time_cards|timeCards|
|**--time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--time-off-requests**|array||time_off_requests|timeOffRequests|
|**--times-off**|array|The instances of times off in the schedule.|times_off|timesOff|
|**--approved-location**|object|geoCoordinates|approved_location|approvedLocation|
|**--show-in-teams-search-and-suggestions**|boolean||show_in_teams_search_and_suggestions|showInTeamsSearchAndSuggestions|

#### <a name="usersDeleteChats">Command `az teams user delete-chat`</a>

##### <a name="ParametersusersDeleteChats">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteJoinedTeams">Command `az teams user delete-joined-team`</a>

##### <a name="ParametersusersDeleteJoinedTeams">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteTeamwork">Command `az teams user delete-teamwork`</a>

##### <a name="ParametersusersDeleteTeamwork">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListChats">Command `az teams user list-chat`</a>

##### <a name="ParametersusersListChats">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListJoinedTeams">Command `az teams user list-joined-team`</a>

##### <a name="ParametersusersListJoinedTeams">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetChats">Command `az teams user show-chat`</a>

##### <a name="ParametersusersGetChats">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetJoinedTeams">Command `az teams user show-joined-team`</a>

##### <a name="ParametersusersGetJoinedTeams">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetTeamwork">Command `az teams user show-teamwork`</a>

##### <a name="ParametersusersGetTeamwork">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateChats">Command `az teams user update-chat`</a>

##### <a name="ParametersusersUpdateChats">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--topic**|string||topic|topic|
|**--installed-apps**|array||installed_apps|installedApps|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--tabs**|array||tabs|tabs|

#### <a name="usersUpdateJoinedTeams">Command `az teams user update-joined-team`</a>

##### <a name="ParametersusersUpdateJoinedTeams">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--is-membership-limited-to-owners**|boolean||is_membership_limited_to_owners|isMembershipLimitedToOwners|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--owners**|array||owners|owners|
|**--photo**|object|profilePhoto|photo|photo|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--provision-status**|choice||provision_status|provisionStatus|
|**--provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--open-shifts**|array||open_shifts|openShifts|
|**--scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--time-cards**|array||time_cards|timeCards|
|**--time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--time-off-requests**|array||time_off_requests|timeOffRequests|
|**--times-off**|array|The instances of times off in the schedule.|times_off|timesOff|
|**--approved-location**|object|geoCoordinates|approved_location|approvedLocation|
|**--show-in-teams-search-and-suggestions**|boolean||show_in_teams_search_and_suggestions|showInTeamsSearchAndSuggestions|

#### <a name="usersUpdateTeamwork">Command `az teams user update-teamwork`</a>

##### <a name="ParametersusersUpdateTeamwork">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--installed-apps**|array|The apps installed in the personal scope of this user.|installed_apps|installedApps|

### group `az teams user-teamwork`
#### <a name="users.teamworkCreateInstalledApps">Command `az teams user-teamwork create-installed-app`</a>

##### <a name="Parametersusers.teamworkCreateInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--azure-ad-app-id**|string||azure_ad_app_id|azureADAppId|
|**--description**|string||description|description|
|**--display-name**|string|The name of the app provided by the app developer.|display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--shortdescription**|string||shortdescription|shortdescription|
|**--teams-app-id**|string|The ID from the Teams app manifest.|teams_app_id|teamsAppId|
|**--version**|string|The version number of the application.|version|version|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--id1**|string|Read-only.|id1|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|
|**--id2**|string|Read-only.|id2|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--topic**|string||topic|topic|
|**--installed-apps**|array||installed_apps|installedApps|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--tabs**|array||tabs|tabs|

#### <a name="users.teamworkDeleteInstalledApps">Command `az teams user-teamwork delete-installed-app`</a>

##### <a name="Parametersusers.teamworkDeleteInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-scope-teams-app-installation-id**|string|key: id of userScopeTeamsAppInstallation|user_scope_teams_app_installation_id|userScopeTeamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.teamworkListInstalledApps">Command `az teams user-teamwork list-installed-app`</a>

##### <a name="Parametersusers.teamworkListInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.teamworkGetInstalledApps">Command `az teams user-teamwork show-installed-app`</a>

##### <a name="Parametersusers.teamworkGetInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-scope-teams-app-installation-id**|string|key: id of userScopeTeamsAppInstallation|user_scope_teams_app_installation_id|userScopeTeamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.teamworkUpdateInstalledApps">Command `az teams user-teamwork update-installed-app`</a>

##### <a name="Parametersusers.teamworkUpdateInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-scope-teams-app-installation-id**|string|key: id of userScopeTeamsAppInstallation|user_scope_teams_app_installation_id|userScopeTeamsAppInstallation-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--azure-ad-app-id**|string||azure_ad_app_id|azureADAppId|
|**--description**|string||description|description|
|**--display-name**|string|The name of the app provided by the app developer.|display_name|displayName|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--shortdescription**|string||shortdescription|shortdescription|
|**--teams-app-id**|string|The ID from the Teams app manifest.|teams_app_id|teamsAppId|
|**--version**|string|The version number of the application.|version|version|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--id1**|string|Read-only.|id1|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|
|**--id2**|string|Read-only.|id2|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-updated-date-time**|date-time||last_updated_date_time|lastUpdatedDateTime|
|**--topic**|string||topic|topic|
|**--installed-apps**|array||installed_apps|installedApps|
|**--members**|array||members|members|
|**--messages**|array||messages|messages|
|**--tabs**|array||tabs|tabs|

### group `az teams user-teamwork-installed-app`
#### <a name="users.teamwork.installedAppsDeleteRefChat">Command `az teams user-teamwork-installed-app delete-ref-chat`</a>

##### <a name="Parametersusers.teamwork.installedAppsDeleteRefChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-scope-teams-app-installation-id**|string|key: id of userScopeTeamsAppInstallation|user_scope_teams_app_installation_id|userScopeTeamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.teamwork.installedAppsSetRefChat">Command `az teams user-teamwork-installed-app set-ref-chat`</a>

##### <a name="Parametersusers.teamwork.installedAppsSetRefChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-scope-teams-app-installation-id**|string|key: id of userScopeTeamsAppInstallation|user_scope_teams_app_installation_id|userScopeTeamsAppInstallation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="users.teamwork.installedAppsGetChat">Command `az teams user-teamwork-installed-app show-chat`</a>

##### <a name="Parametersusers.teamwork.installedAppsGetChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-scope-teams-app-installation-id**|string|key: id of userScopeTeamsAppInstallation|user_scope_teams_app_installation_id|userScopeTeamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.teamwork.installedAppsGetRefChat">Command `az teams user-teamwork-installed-app show-ref-chat`</a>

##### <a name="Parametersusers.teamwork.installedAppsGetRefChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-scope-teams-app-installation-id**|string|key: id of userScopeTeamsAppInstallation|user_scope_teams_app_installation_id|userScopeTeamsAppInstallation-id|

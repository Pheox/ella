
# tohle smazat ze south dumpu, abychom meli cistou databazi
delete from auth_permission;
delete from auth_user;
delete from cdnclient_format;
delete from django_content_type;
delete from django_site;


# tohle mazat z ostreho dumpu pred vysosanim dat

# pozor na id 2347 (slug misa je tam triplicita)
update core_author a, core_author b set a.slug = concat(a.slug, '_') where a.slug = b.slug and a.id < b.id;
update core_author a, core_author b set a.slug = concat(a.slug, '_') where a.slug = b.slug and a.id < b.id;

# uz neni
drop table core_dependency;

# pk je neco jineho
alter table core_hitcount drop column id;

# tohle delal honza, neni pro to model
drop table discussions_question;

# tahle appka se nepouziva
drop table `discussions_bannedstring`;
drop table `discussions_banneduser`;
drop table `discussions_postviewed`;
drop table `discussions_topicthread`;
drop table `discussions_topic`;

# nepouzivame
drop table ellaadmin_categoryuserrole;
drop table ellaadmin_siteuserrole;

# nepouzivame
drop table encoder_format;
drop table encoder_formattedfile;



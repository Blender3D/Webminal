title: update 

that should have displayed some error message.

Because you (yes,its you not my fault :P) didn't 
tell 'what' column to update and 'where' to 
update.

OMG,we entered some wrong data for earth,It appears recently
it  moved to 2 place in our solar system! need proof? go 
outside at 13:00.So we need to edit that record. How to do 
that? Here comes 'update' to your rescue.

        update planets set position=2 
	  where name="earth";

Now go and view results again via select query.
Now its time to trash something.Lets delete mars!

Say good bye to "Spirit".We going to destory it.

        delete from planets where name="mars";


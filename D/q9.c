NodeRef xp = head;
while(xp->next != head){
    printf("%d", xp->k);
    xp = xp->next;
}

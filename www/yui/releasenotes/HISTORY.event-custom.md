Custom Event Infrastructure Change History
==========================================

3.6.0
-----

 * Fixed memory consumption issue where Y.Do's internal touched object cache, 
   Y.Do.objs, would never release object references.

   The Y.Do.objs property has been deprecated as of 3.6.0, and will be null.

   The cached state previously stored in Y.Do.objs has been moved onto the
   AOP'd object itself, in the *private* `_yuiaop` property.

   The only reason `_yuiaop` is mentioned here, is to provide a temporary 
   migration path for users who may have been using Y.Do.objs. If you are using 
   this property, please file a ticket with the use case, and we'll look at 
   addressing the use case formally, while not impacting GC.

3.5.1
-----

  * No changes.

3.5.0
-----

  * Multiple calls to target.publish({ ... }) now work [Ticket #2531671]

3.4.1
-----

  * onceAfter (added in 3.4.0) now works for array and object signatures.
    [Ticket #2531121]

3.4.0
-----

  * Custom events published from `Y` no longer bubble by default.

3.3.0
-----

  * Undocumented and poorly named `each()` method on EventHandle changed to
    `batch()`.

  * After listeners for events fired in a `defaultFn` or listener are queued in
    the correct order.

  * Added `Y.Do.originalRetVal` and `Y.Do.currentRetVal` statics accessible by
    `Y.Do.after()` subscribers.

  * Exposed the previously private `EventTarget.parseType`.

3.2.0
-----

  * Fixed `defaultTargetOnly` publish configuration.

  * `detach()` now decrements `subCount`/`afterCount`.

  * Detaching via category no longer affects subscriptions on other objects.

3.1.1
-----

  * No changes.

3.1.0
-----

  * Wildcard prefix subscriptions supported: `target.on('*:click', …)` will be
    notified when `tree:click`, `tab:click`, etc are fired.

  * Added `EventTarget::once`, which is equivalent to `on()`, except the
    listener automatically detaches itself once executed.

  * Added event monitoring. When configured, an `EventTarget` will emit events
    for `publish()`, `attach()`, `fire()`, and `detach()` operations on the
    hosted events.

  * `EventTarget::on`'s `type` parameter is overloaded to accept arrays and
    objects for attaching multiple types at once.

  * `EventTarget::detach` returns the event target like the API docs already
    stated.

  * Events can now be configured to execute the `defaultFn` only on the targeted
    object, not on the bubble targets.

  * The event order has been reworked so that the after listeners for the entire
    event stack execute after all `defaultFn` across the entire bubble stack.

3.0.0
-----

  * Broken into core base and complex modules.

  * `broadcast` works for simple events.

  * If configured to return an `EventHandle`, the return value will always be a
    single object, regardless of how many listeners were attached. Previously,
    multiple listeners provided an array of detach handles.

3.0.0beta1
----------

  * [!] Exposed methods are `on()` for the before moment, `after()` for the
    after moment, and `detach()` for unsubscribe. `subscribe()`, `before()`,
    `unsubscribe()`, and corresponding methods are deprecated.
  
  * Implemented the `broadcast` flag:
  
    * `broadcast = 1`: local, accessible via `Y.on('prefix:event')`.
    * `broadcast = 2`: global, accessible via `Y.on()` or globally via
      `Y.Global.on('prefix:event')`.
  
    Broadcast listeners cannot effect the `defaultFn` or host subscribers (so
    are in effect, after listeners), although this is still possible by added
    either `Y` or `Y.Global` as `EventTarget`s.

  * Moved `event-custom` out of `event` package.

  * `EventTarget` accepts a `prefix` configuration. This is used in all exposed
    methods to handle shortcuts to event names, e.g., `'click'` and
    `'menu:click'` are the same if the prefix is `'menu'`.

  * Event type accepts a event category which can be used to detach events:
  
        Y.on('category|prefix:event', fn);
        Y.detach('category|prefix:event');
        Y.detach('category|*');

  * Added `chain` config to events that makes the return value the event target
    rather than a detach handle. Use with the detach category prefix.

  * The `type` parameter can be an object containing multiple events to attach:
  
        Y.on({ 'event1': fn1, 'event2': fn2 });

  * `Y.fire` payload for event facades can be another facade or a custom event.